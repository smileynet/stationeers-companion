"""Steam Workshop scraper for IC10 code examples via SteamCMD."""

import argparse
import json
import re
import shutil
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

from . import config
from .github_scraper import IC10Script

console = Console()

# Steam Workshop constants
STEAM_APPID = 544550  # Stationeers
STEAM_WORKSHOP_URL = "https://steamcommunity.com/sharedfiles/filedetails"
STEAM_SEARCH_URL = "https://steamcommunity.com/workshop/browse"


class SteamCMDNotFoundError(Exception):
    """Raised when SteamCMD is not installed."""

    pass


@dataclass
class WorkshopMetadata:
    """Metadata for a Steam Workshop item."""

    workshop_id: int
    title: str
    author: str
    description: str
    url: str
    last_updated: Optional[datetime] = None
    rating: Optional[float] = None
    subscribers: int = 0
    is_compatible: bool = True
    compatibility_note: str = ""
    tags: list[str] = field(default_factory=list)


class SteamScraper:
    """Download IC10 scripts from Steam Workshop via SteamCMD."""

    def __init__(self, cache_dir: Optional[Path] = None):
        self.cache_dir = cache_dir or config.PROJECT_ROOT / ".cache" / "steam"
        self.metadata_cache = self.cache_dir / "metadata"
        self.content_cache = self.cache_dir / "content"
        self.session = requests.Session()
        self.session.headers["User-Agent"] = config.USER_AGENT

        # Ensure cache directories exist
        self.metadata_cache.mkdir(parents=True, exist_ok=True)
        self.content_cache.mkdir(parents=True, exist_ok=True)

        # Verify SteamCMD is available
        self._verify_steamcmd()

    def _verify_steamcmd(self) -> None:
        """Check SteamCMD is installed, raise with install instructions if not."""
        steamcmd_path = shutil.which("steamcmd")
        if steamcmd_path is None:
            raise SteamCMDNotFoundError(
                "SteamCMD is not installed or not in PATH.\n\n"
                "Install instructions:\n"
                "  Ubuntu/Debian: sudo apt install steamcmd\n"
                "  Arch: yay -S steamcmd\n"
                "  Manual: https://developer.valvesoftware.com/wiki/SteamCMD\n\n"
                "After installation, ensure 'steamcmd' is in your PATH."
            )
        self.steamcmd_path = steamcmd_path

    def extract_workshop_id(self, url_or_id: str) -> Optional[int]:
        """Extract workshop ID from URL or direct ID string.

        Handles:
        - https://steamcommunity.com/sharedfiles/filedetails/?id=2960497565
        - 2960497565
        """
        # Try direct integer
        try:
            return int(url_or_id)
        except ValueError:
            pass

        # Try URL parsing
        parsed = urlparse(url_or_id)
        if "steamcommunity.com" in parsed.netloc:
            query = parse_qs(parsed.query)
            if "id" in query:
                try:
                    return int(query["id"][0])
                except (ValueError, IndexError):
                    pass

        return None

    def get_workshop_metadata(
        self, workshop_id: int, use_cache: bool = True
    ) -> Optional[WorkshopMetadata]:
        """Scrape Steam page for title, author, description, date."""
        cache_file = self.metadata_cache / f"{workshop_id}.json"

        # Check cache (valid for 7 days)
        if use_cache and cache_file.exists():
            cache_age = time.time() - cache_file.stat().st_mtime
            if cache_age < 7 * 24 * 60 * 60:  # 7 days
                try:
                    data = json.loads(cache_file.read_text())
                    return WorkshopMetadata(
                        workshop_id=data["workshop_id"],
                        title=data["title"],
                        author=data["author"],
                        description=data["description"],
                        url=data["url"],
                        last_updated=datetime.fromisoformat(data["last_updated"])
                        if data.get("last_updated")
                        else None,
                        rating=data.get("rating"),
                        subscribers=data.get("subscribers", 0),
                        is_compatible=data.get("is_compatible", True),
                        compatibility_note=data.get("compatibility_note", ""),
                        tags=data.get("tags", []),
                    )
                except (json.JSONDecodeError, KeyError):
                    pass

        # Fetch from Steam
        url = f"{STEAM_WORKSHOP_URL}/?id={workshop_id}"
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            time.sleep(config.REQUEST_DELAY)
        except requests.RequestException as e:
            console.print(f"[red]Failed to fetch workshop page: {e}[/red]")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Check if item exists
        error_div = soup.find("div", class_="error_ctn")
        if error_div:
            console.print(f"[yellow]Workshop item {workshop_id} not found[/yellow]")
            return None

        # Extract title
        title_elem = soup.find("div", class_="workshopItemTitle")
        title = title_elem.get_text(strip=True) if title_elem else f"Item {workshop_id}"

        # Extract author
        author_elem = soup.find("div", class_="friendBlockContent")
        author = "Unknown"
        if author_elem:
            author_text = author_elem.get_text(strip=True)
            # Author name is typically the first line
            author = author_text.split("\n")[0].strip()

        # Extract description
        desc_elem = soup.find("div", class_="workshopItemDescription")
        description = desc_elem.get_text(strip=True)[:500] if desc_elem else ""

        # Extract last updated date
        last_updated = None
        details_table = soup.find("div", class_="detailsStatsContainerRight")
        if details_table:
            date_elem = details_table.find("div", class_="detailsStatRight")
            if date_elem:
                date_text = date_elem.get_text(strip=True)
                last_updated = self._parse_steam_date(date_text)

        # Extract subscriber count
        subscribers = 0
        stats_table = soup.find_all("td", class_="workshopItemTableRowData")
        for stat in stats_table:
            text = stat.get_text(strip=True)
            if text.replace(",", "").isdigit():
                subscribers = int(text.replace(",", ""))
                break

        # Extract tags
        tags = []
        tag_elems = soup.find_all("a", class_="workshopItemTag")
        for tag in tag_elems:
            tags.append(tag.get_text(strip=True))

        # Check compatibility
        is_compatible = True
        compatibility_note = ""

        # Check for "Incompatible" banner
        compat_warning = soup.find("div", class_="incompatibleItem")
        if compat_warning:
            is_compatible = False
            compatibility_note = "Marked as incompatible with current game version"

        # Check date for version compatibility
        if last_updated:
            # Trading Update III was Dec 2022
            breaking_change_date = datetime(2022, 12, 1)
            if last_updated < breaking_change_date:
                is_compatible = False
                compatibility_note = (
                    f"Last updated {last_updated.strftime('%b %Y')} - "
                    "predates Trading Update III (Dec 2022)"
                )

        metadata = WorkshopMetadata(
            workshop_id=workshop_id,
            title=title,
            author=author,
            description=description,
            url=url,
            last_updated=last_updated,
            rating=None,  # Rating requires more complex scraping
            subscribers=subscribers,
            is_compatible=is_compatible,
            compatibility_note=compatibility_note,
            tags=tags,
        )

        # Cache the result
        cache_data = {
            "workshop_id": metadata.workshop_id,
            "title": metadata.title,
            "author": metadata.author,
            "description": metadata.description,
            "url": metadata.url,
            "last_updated": metadata.last_updated.isoformat()
            if metadata.last_updated
            else None,
            "rating": metadata.rating,
            "subscribers": metadata.subscribers,
            "is_compatible": metadata.is_compatible,
            "compatibility_note": metadata.compatibility_note,
            "tags": metadata.tags,
        }
        cache_file.write_text(json.dumps(cache_data, indent=2))

        return metadata

    def _parse_steam_date(self, date_text: str) -> Optional[datetime]:
        """Parse Steam's date format (e.g., 'Dec 15, 2023 @ 10:30am')."""
        # Remove @ and time portion for simpler parsing
        date_text = re.sub(r"@.*", "", date_text).strip()

        formats = [
            "%b %d, %Y",  # Dec 15, 2023
            "%d %b, %Y",  # 15 Dec, 2023
            "%b %d",  # Dec 15 (current year)
        ]

        for fmt in formats:
            try:
                parsed = datetime.strptime(date_text, fmt)
                # If no year in format, assume current year
                if "%Y" not in fmt:
                    parsed = parsed.replace(year=datetime.now().year)
                return parsed
            except ValueError:
                continue

        return None

    def download_item(self, workshop_id: int, force: bool = False) -> Optional[Path]:
        """Use SteamCMD to download workshop item, return content path."""
        content_dir = self.content_cache / str(workshop_id)

        # Check if already downloaded
        if not force and content_dir.exists():
            ic10_files = list(content_dir.rglob("*.ic10"))
            if ic10_files:
                console.print(f"  [dim]Using cached download for {workshop_id}[/dim]")
                return content_dir

        console.print(f"  [cyan]Downloading workshop item {workshop_id}...[/cyan]")

        # Build SteamCMD command
        cmd = [
            self.steamcmd_path,
            "+force_install_dir",
            str(self.content_cache),
            "+login",
            "anonymous",
            "+workshop_download_item",
            str(STEAM_APPID),
            str(workshop_id),
            "+quit",
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
            )

            # SteamCMD puts content in a specific structure
            downloaded_path = (
                self.content_cache
                / "steamapps"
                / "workshop"
                / "content"
                / str(STEAM_APPID)
                / str(workshop_id)
            )

            if downloaded_path.exists():
                # Move to our simpler cache structure
                if content_dir.exists():
                    shutil.rmtree(content_dir)
                shutil.move(str(downloaded_path), str(content_dir))
                console.print(f"  [green]Downloaded to {content_dir}[/green]")
                return content_dir
            else:
                console.print(
                    "  [yellow]Download completed but content not found[/yellow]"
                )
                if result.stderr:
                    console.print(f"  [dim]{result.stderr[:200]}[/dim]")
                return None

        except subprocess.TimeoutExpired:
            console.print(f"  [red]Download timed out for {workshop_id}[/red]")
            return None
        except subprocess.SubprocessError as e:
            console.print(f"  [red]Download failed: {e}[/red]")
            return None

    def find_ic10_files(self, content_path: Path) -> list[Path]:
        """Find .ic10 files in downloaded content."""
        if not content_path.exists():
            return []

        # Look for .ic10 files
        ic10_files = list(content_path.rglob("*.ic10"))

        # Also check for .mips files
        mips_files = list(content_path.rglob("*.mips"))
        ic10_files.extend(mips_files)

        # Check for instruction.xml files (Stationeers Workshop format)
        for xml_file in content_path.rglob("instruction.xml"):
            ic10_files.append(xml_file)

        # Also check for files without extension that might be scripts
        # (Some workshop items just have the script as a text file)
        for txt_file in content_path.rglob("*.txt"):
            content = txt_file.read_text(errors="ignore")
            # Check if it looks like IC10 code
            if self._looks_like_ic10(content):
                ic10_files.append(txt_file)

        return ic10_files

    def _extract_from_instruction_xml(self, xml_path: Path) -> Optional[str]:
        """Extract IC10 code from instruction.xml format."""
        import xml.etree.ElementTree as ET

        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            instructions_elem = root.find("Instructions")
            if instructions_elem is not None and instructions_elem.text:
                return instructions_elem.text
        except Exception as e:
            console.print(f"  [dim]XML parse error: {e}[/dim]")
        return None

    def _looks_like_ic10(self, content: str) -> bool:
        """Check if content looks like IC10 code."""
        ic10_patterns = [
            r"^\s*alias\s+\w+\s+[rd]",  # alias declarations
            r"^\s*define\s+\w+\s+",  # define statements
            r"^\s*l\s+r\d+\s+d\d+",  # load instructions
            r"^\s*s\s+d\d+\s+\w+",  # store instructions
            r"^\s*yield\s*$",  # yield instruction
            r"^\s*j\s+\w+\s*$",  # jump instruction
        ]

        lines = content.split("\n")
        matches = 0
        for line in lines[:50]:  # Check first 50 lines
            for pattern in ic10_patterns:
                if re.match(pattern, line, re.IGNORECASE):
                    matches += 1
                    break

        # If at least 3 IC10-like patterns found, probably IC10 code
        return matches >= 3

    def collect_script(self, workshop_id: int) -> Optional[IC10Script]:
        """Full workflow: metadata + download + parse."""
        console.print(f"[bold]Collecting workshop item {workshop_id}...[/bold]")

        # Get metadata
        metadata = self.get_workshop_metadata(workshop_id)
        if not metadata:
            return None

        # Download content
        content_path = self.download_item(workshop_id)
        if not content_path:
            return None

        # Find IC10 files
        ic10_files = self.find_ic10_files(content_path)
        if not ic10_files:
            console.print(
                f"  [yellow]No IC10 files found in workshop item {workshop_id}[/yellow]"
            )
            return None

        # Use the first IC10 file found
        script_file = ic10_files[0]

        # Handle instruction.xml format
        if script_file.name == "instruction.xml":
            content = self._extract_from_instruction_xml(script_file)
            if not content:
                console.print(
                    "  [yellow]Could not extract code from instruction.xml[/yellow]"
                )
                return None
        else:
            content = script_file.read_text(errors="ignore")

        # Create IC10Script
        script = IC10Script(
            name=metadata.title,
            content=content,
            source_url=metadata.url,
            repo=f"Steam Workshop ({metadata.author})",
            path=str(script_file.relative_to(content_path)),
        )

        # Analyze and categorize
        self._analyze_script(script, metadata)

        return script

    def _analyze_script(self, script: IC10Script, metadata: WorkshopMetadata) -> None:
        """Analyze script content to extract metadata."""
        content_lower = script.content.lower()
        name_lower = script.name.lower()

        # Determine category based on keywords
        category_scores: dict[str, int] = {}
        for category, keywords in config.CATEGORY_KEYWORDS.items():
            score = 0
            for keyword in keywords:
                if keyword in content_lower:
                    score += 1
                if keyword in name_lower:
                    score += 2
            if score > 0:
                category_scores[category] = score

        if category_scores:
            script.category = max(category_scores, key=category_scores.get)

        # Use metadata description if no description extracted
        if not script.description and metadata.description:
            script.description = metadata.description[:200]

        # Extract device aliases
        device_pattern = re.compile(r"alias\s+(\w+)\s+(d[0-5b])", re.IGNORECASE)
        for match in device_pattern.finditer(script.content):
            alias_name = match.group(1)
            device_port = match.group(2)
            script.devices.append(f"{device_port} = {alias_name}")

    def search_workshop(self, query: str, limit: int = 10) -> list[WorkshopMetadata]:
        """Search Steam Workshop for IC10 scripts matching query."""
        console.print(f"[bold]Searching Steam Workshop for '{query}'...[/bold]")

        # Steam Workshop search URL
        search_url = (
            f"https://steamcommunity.com/workshop/browse/"
            f"?appid={STEAM_APPID}&searchtext={query}&browsesort=textsearch"
        )

        try:
            response = self.session.get(search_url, timeout=30)
            response.raise_for_status()
            time.sleep(config.REQUEST_DELAY)
        except requests.RequestException as e:
            console.print(f"[red]Search failed: {e}[/red]")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # Find workshop items
        items = soup.find_all("div", class_="workshopItem")
        results = []

        for item in items[:limit]:
            # Extract workshop ID from link
            link = item.find("a", class_="ugc")
            if not link:
                continue

            href = link.get("href", "")
            workshop_id = self.extract_workshop_id(href)
            if not workshop_id:
                continue

            # Get metadata for this item
            metadata = self.get_workshop_metadata(workshop_id)
            if metadata:
                results.append(metadata)

        console.print(f"  Found {len(results)} results")
        return results

    def collect_from_search(self, query: str, limit: int = 10) -> list[IC10Script]:
        """Search + download workflow for batch collection."""
        results = self.search_workshop(query, limit)

        scripts = []
        for metadata in results:
            script = self.collect_script(metadata.workshop_id)
            if script:
                scripts.append(script)

        return scripts

    def save_script(self, script: IC10Script, output_dir: Path) -> None:
        """Save script with attribution header."""
        output_dir.mkdir(parents=True, exist_ok=True)

        # Clean filename
        filename = re.sub(r"[^a-zA-Z0-9_-]", "-", script.name.lower())
        filename = re.sub(r"-+", "-", filename).strip("-")
        filepath = output_dir / f"{filename}.ic10"

        # Generate header
        header_lines = [
            "# " + "=" * 50,
            f"# {script.name}",
            "# " + "=" * 50,
            f"# Source: {script.source_url}",
            f"# Author: {script.repo}",
            f"# Category: {script.category}",
            "#",
        ]

        if script.description:
            header_lines.append(f"# Description: {script.description}")
            header_lines.append("#")

        if script.devices:
            header_lines.append("# Devices:")
            for device in script.devices:
                header_lines.append(f"#   {device}")
            header_lines.append("#")

        header_lines.append("# " + "=" * 50)
        header_lines.append("")

        content = "\n".join(header_lines) + script.content
        filepath.write_text(content)
        console.print(f"  Saved: {filepath}")


def display_metadata_table(items: list[WorkshopMetadata]) -> None:
    """Display workshop items in a formatted table."""
    table = Table(title="Steam Workshop Results")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="white")
    table.add_column("Author", style="green")
    table.add_column("Updated", style="yellow")
    table.add_column("Status", style="magenta")

    for item in items:
        status = (
            "[green]Compatible[/green]" if item.is_compatible else "[red]Outdated[/red]"
        )
        updated = (
            item.last_updated.strftime("%Y-%m-%d") if item.last_updated else "Unknown"
        )
        table.add_row(
            str(item.workshop_id),
            item.title[:40] + "..." if len(item.title) > 40 else item.title,
            item.author[:20],
            updated,
            status,
        )

    console.print(table)


def main():
    """Run the Steam Workshop scraper."""
    parser = argparse.ArgumentParser(
        description="Download IC10 scripts from Steam Workshop"
    )
    parser.add_argument(
        "--id",
        type=int,
        help="Workshop item ID to download",
    )
    parser.add_argument(
        "--url",
        type=str,
        help="Workshop item URL to download",
    )
    parser.add_argument(
        "--search",
        type=str,
        help="Search query for finding workshop items",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of search results (default: 10)",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Only list results, don't download",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output directory for downloaded scripts",
    )

    args = parser.parse_args()

    if not any([args.id, args.url, args.search]):
        parser.error("Must specify --id, --url, or --search")

    try:
        scraper = SteamScraper()
    except SteamCMDNotFoundError as e:
        console.print(f"[red]Error:[/red] {e}")
        return 1

    output_dir = Path(args.output) if args.output else config.EXAMPLES_OUTPUT

    # Handle single item fetch
    if args.id or args.url:
        workshop_id = args.id or scraper.extract_workshop_id(args.url)
        if not workshop_id:
            console.print("[red]Could not extract workshop ID[/red]")
            return 1

        if args.list_only:
            metadata = scraper.get_workshop_metadata(workshop_id)
            if metadata:
                display_metadata_table([metadata])
        else:
            script = scraper.collect_script(workshop_id)
            if script:
                scraper.save_script(script, output_dir / script.category)
                console.print(
                    f"\n[green]Successfully downloaded: {script.name}[/green]"
                )
            else:
                console.print("[yellow]No IC10 script found in workshop item[/yellow]")

    # Handle search
    elif args.search:
        if args.list_only:
            results = scraper.search_workshop(args.search, args.limit)
            if results:
                display_metadata_table(results)
            else:
                console.print("[yellow]No results found[/yellow]")
        else:
            scripts = scraper.collect_from_search(args.search, args.limit)
            if scripts:
                for script in scripts:
                    scraper.save_script(script, output_dir / script.category)
                console.print(f"\n[green]Downloaded {len(scripts)} scripts[/green]")
            else:
                console.print("[yellow]No IC10 scripts found[/yellow]")

    console.print("\n[bold green]Steam Workshop scraping complete![/bold green]")
    return 0


if __name__ == "__main__":
    exit(main())
