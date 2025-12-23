"""Stationeers Wiki scraper for IC10 reference documentation."""

import argparse
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from . import config

console = Console()


@dataclass
class InstructionDoc:
    """Documentation for an IC10 instruction."""

    name: str
    category: str
    syntax: str = ""
    description: str = ""
    parameters: list[dict] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class DeviceDoc:
    """Documentation for a Stationeers device."""

    name: str
    category: str
    prefab_hash: Optional[int] = None
    power_usage: Optional[int] = None
    readable_logic: list[dict] = field(default_factory=list)
    writable_logic: list[dict] = field(default_factory=list)
    slots: list[dict] = field(default_factory=list)
    description: str = ""


class WikiScraper:
    """Scraper for stationeers-wiki.com content."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = config.USER_AGENT
        self.cache_dir = config.PROJECT_ROOT / ".cache"
        self.cache_dir.mkdir(exist_ok=True)

    def _get_page(self, path: str) -> Optional[BeautifulSoup]:
        """Fetch a wiki page with caching and rate limiting."""
        cache_file = self.cache_dir / f"{path.replace('/', '_')}.html"

        # Check cache
        if cache_file.exists():
            console.print(f"  [dim]Using cached: {path}[/dim]")
            return BeautifulSoup(cache_file.read_text(), "html.parser")

        # Fetch from wiki
        url = f"{config.WIKI_BASE_URL}/{path}"
        console.print(f"  [cyan]Fetching: {url}[/cyan]")

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            # Cache the response
            cache_file.write_text(response.text)

            # Rate limit
            time.sleep(config.REQUEST_DELAY)

            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            console.print(f"  [red]Error fetching {url}: {e}[/red]")
            return None

    def scrape_ic10_reference(self) -> dict[str, list[InstructionDoc]]:
        """Scrape IC10 instruction reference from wiki."""
        console.print("[bold]Scraping IC10 instruction reference...[/bold]")

        # Fetch the main IC10 page
        soup = self._get_page("IC10")
        if not soup:
            return {}

        instructions_by_category: dict[str, list[InstructionDoc]] = {}

        # Parse instructions from the page
        # The wiki has instruction tables organized by category
        for category, instr_list in config.INSTRUCTION_CATEGORIES.items():
            instructions_by_category[category] = []

            for instr_name in instr_list:
                doc = self._parse_instruction(soup, instr_name, category)
                if doc:
                    instructions_by_category[category].append(doc)

        return instructions_by_category

    def _parse_instruction(
        self, soup: BeautifulSoup, name: str, category: str
    ) -> Optional[InstructionDoc]:
        """Parse a single instruction from the wiki page."""
        doc = InstructionDoc(name=name, category=category)

        # Look for instruction in tables
        # The wiki typically has tables with instruction info
        tables = soup.find_all("table", class_="wikitable")

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all(["td", "th"])
                if cells and cells[0].get_text(strip=True).lower() == name.lower():
                    # Found the instruction row
                    if len(cells) >= 2:
                        doc.syntax = cells[0].get_text(strip=True)
                    if len(cells) >= 3:
                        doc.description = cells[1].get_text(strip=True)
                    break

        # If we didn't find it in tables, try to find it in text
        if not doc.description:
            # Look for the instruction name in code blocks or definitions
            code_blocks = soup.find_all(["code", "pre"])
            for block in code_blocks:
                text = block.get_text()
                if name in text.split():
                    # Extract context around the instruction
                    doc.description = f"IC10 instruction: {name}"
                    break

        # Set default syntax based on category patterns
        if not doc.syntax:
            doc.syntax = self._get_default_syntax(name, category)

        return doc

    def _get_default_syntax(self, name: str, category: str) -> str:
        """Get default syntax pattern for an instruction."""
        patterns = {
            "math": f"{name} r? a b",
            "logic": f"{name} r? device logicType",
            "batch": f"{name} r? hash logicType mode",
            "comparison": f"{name} r? a b",
            "branching": f"{name} a b label",
            "bitwise": f"{name} r? a b",
            "stack": f"{name} r?",
            "utility": f"{name}",
        }

        # Special cases
        special = {
            "l": "l r? device logicType",
            "s": "s device logicType value",
            "ls": "ls r? device slot logicType",
            "ss": "ss device slot logicType value",
            "lb": "lb r? hash logicType mode",
            "sb": "sb hash logicType value",
            "j": "j label",
            "jr": "jr offset",
            "jal": "jal label",
            "beq": "beq a b label",
            "bne": "bne a b label",
            "bgt": "bgt a b label",
            "blt": "blt a b label",
            "alias": "alias name register",
            "define": "define name value",
            "move": "move r? value",
            "yield": "yield",
            "sleep": "sleep seconds",
            "hcf": "hcf",
            "select": "select r? cond a b",
            "push": "push value",
            "pop": "pop r?",
            "peek": "peek r?",
            "abs": "abs r? value",
            "sqrt": "sqrt r? value",
            "not": "not r? value",
        }

        return special.get(name, patterns.get(category, name))

    def scrape_device(self, device_name: str) -> Optional[DeviceDoc]:
        """Scrape a single device page from the wiki."""
        # Convert device name to wiki URL format
        page_name = device_name.replace(" ", "_")
        soup = self._get_page(page_name)

        if not soup:
            return None

        # Determine category from device name
        category = self._categorize_device(device_name)

        doc = DeviceDoc(name=device_name, category=category)

        # Parse the infobox for device properties
        infobox = soup.find("table", class_="infobox")
        if infobox:
            self._parse_infobox(infobox, doc)

        # Look for Logic section
        logic_header = soup.find(
            ["h2", "h3"], string=re.compile(r"Logic|IC10", re.IGNORECASE)
        )
        if logic_header:
            self._parse_logic_section(logic_header, doc)

        # Look for logic tables directly
        if not doc.readable_logic and not doc.writable_logic:
            self._parse_logic_tables(soup, doc)

        return doc

    def _categorize_device(self, device_name: str) -> str:
        """Categorize a device based on its name."""
        name_lower = device_name.lower()

        if any(
            x in name_lower
            for x in ["vent", "pump", "sensor", "filter", "conditioner", "pipe"]
        ):
            return "atmospheric"
        if any(
            x in name_lower
            for x in ["solar", "battery", "apc", "generator", "transformer"]
        ):
            return "power"
        if any(
            x in name_lower
            for x in ["furnace", "printer", "lathe", "centrifuge", "bender"]
        ):
            return "fabrication"
        if any(
            x in name_lower
            for x in ["ic", "logic", "memory", "switch", "reader", "writer"]
        ):
            return "logic"
        if any(x in name_lower for x in ["door", "airlock", "gate"]):
            return "doors"
        return "other"

    def _parse_infobox(self, infobox: BeautifulSoup, doc: DeviceDoc) -> None:
        """Parse device infobox for properties."""
        rows = infobox.find_all("tr")
        for row in rows:
            header = row.find("th")
            data = row.find("td")
            if header and data:
                header_text = header.get_text(strip=True).lower()
                data_text = data.get_text(strip=True)

                if "hash" in header_text:
                    try:
                        doc.prefab_hash = int(data_text.replace(",", ""))
                    except ValueError:
                        pass
                elif "power" in header_text:
                    try:
                        doc.power_usage = int(re.search(r"\d+", data_text).group())
                    except (ValueError, AttributeError):
                        pass

    def _parse_logic_section(self, header: BeautifulSoup, doc: DeviceDoc) -> None:
        """Parse the Logic section after a header."""
        # Find the next table after the Logic header
        next_elem = header.find_next_sibling()
        while next_elem:
            if next_elem.name == "table":
                self._parse_logic_table(next_elem, doc)
                break
            if next_elem.name in ["h2", "h3"]:
                break
            next_elem = next_elem.find_next_sibling()

    def _parse_logic_tables(self, soup: BeautifulSoup, doc: DeviceDoc) -> None:
        """Parse all tables looking for logic information."""
        tables = soup.find_all("table", class_="wikitable")
        for table in tables:
            self._parse_logic_table(table, doc)

    def _parse_logic_table(self, table: BeautifulSoup, doc: DeviceDoc) -> None:
        """Parse a table for logic type information."""
        rows = table.find_all("tr")
        if not rows:
            return

        # Check header row
        header = rows[0]
        header_cells = header.find_all(["th", "td"])
        header_text = [cell.get_text(strip=True).lower() for cell in header_cells]

        # Look for logic type indicators
        has_logic_type = any("logic" in h or "type" in h for h in header_text)
        has_access = any("read" in h or "write" in h or "access" in h for h in header_text)

        if not (has_logic_type or has_access):
            return

        # Parse data rows
        for row in rows[1:]:
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                logic_type = cells[0].get_text(strip=True)
                description = cells[1].get_text(strip=True) if len(cells) > 1 else ""

                # Determine if readable or writable
                access_text = " ".join(cell.get_text(strip=True).lower() for cell in cells)
                is_writable = "write" in access_text or "set" in access_text
                is_readable = "read" in access_text or not is_writable

                entry = {"name": logic_type, "description": description}

                if is_readable:
                    doc.readable_logic.append(entry)
                if is_writable:
                    doc.writable_logic.append(entry)

    def save_instruction_docs(
        self, instructions: dict[str, list[InstructionDoc]]
    ) -> None:
        """Save instruction documentation to markdown files."""
        output_dir = config.INSTRUCTION_OUTPUT
        output_dir.mkdir(parents=True, exist_ok=True)

        console.print(f"\n[bold]Saving to {output_dir}[/bold]")

        # Create index file
        index_content = self._generate_instruction_index(instructions)
        (output_dir / "index.md").write_text(index_content)
        console.print("  Saved: index.md")

        # Create category files
        for category, docs in instructions.items():
            content = self._generate_instruction_category(category, docs)
            filename = f"{category}.md"
            (output_dir / filename).write_text(content)
            console.print(f"  Saved: {filename}")

    def _generate_instruction_index(
        self, instructions: dict[str, list[InstructionDoc]]
    ) -> str:
        """Generate index markdown for all instruction categories."""
        lines = [
            "---",
            "title: IC10 Instructions Reference",
            "---",
            "",
            "# IC10 Instructions Reference",
            "",
            "Complete reference for all IC10 instructions in Stationeers.",
            "",
            "## Categories",
            "",
        ]

        for category, docs in instructions.items():
            title = category.replace("_", " ").title()
            lines.append(f"### [{title}]({category}.md)")
            lines.append("")
            instr_list = ", ".join(f"`{d.name}`" for d in docs[:10])
            if len(docs) > 10:
                instr_list += f", ... ({len(docs)} total)"
            lines.append(instr_list)
            lines.append("")

        return "\n".join(lines)

    def _generate_instruction_category(
        self, category: str, docs: list[InstructionDoc]
    ) -> str:
        """Generate markdown for an instruction category."""
        title = category.replace("_", " ").title()

        lines = [
            "---",
            f"title: {title} Instructions",
            f"category: {category}",
            "---",
            "",
            f"# {title} Instructions",
            "",
        ]

        for doc in docs:
            lines.extend(
                [
                    f"## {doc.name}",
                    "",
                    f"**Syntax**: `{doc.syntax}`",
                    "",
                ]
            )

            if doc.description:
                lines.extend([doc.description, ""])

            if doc.parameters:
                lines.append("**Parameters**:")
                for param in doc.parameters:
                    lines.append(
                        f"- `{param['name']}` ({param.get('type', 'any')}) - "
                        f"{param.get('description', '')}"
                    )
                lines.append("")

            if doc.examples:
                lines.append("**Example**:")
                lines.append("```ic10")
                lines.extend(doc.examples)
                lines.append("```")
                lines.append("")

            if doc.notes:
                lines.extend(["**Notes**:", doc.notes, ""])

            lines.append("---")
            lines.append("")

        return "\n".join(lines)

    def save_device_doc(self, doc: DeviceDoc) -> None:
        """Save device documentation to markdown file."""
        category_dir = config.DEVICE_OUTPUT / doc.category
        category_dir.mkdir(parents=True, exist_ok=True)

        filename = doc.name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        filename = re.sub(r"[^a-z0-9-]", "", filename) + ".md"

        content = self._generate_device_markdown(doc)
        (category_dir / filename).write_text(content)
        console.print(f"  Saved: {doc.category}/{filename}")

    def _generate_device_markdown(self, doc: DeviceDoc) -> str:
        """Generate markdown for a device."""
        lines = [
            "---",
            f"title: {doc.name}",
            f"category: {doc.category}",
        ]

        if doc.prefab_hash:
            lines.append(f"prefab_hash: {doc.prefab_hash}")
        if doc.power_usage:
            lines.append(f"power: {doc.power_usage}")

        lines.extend(["---", "", f"# {doc.name}", ""])

        if doc.description:
            lines.extend([doc.description, ""])

        if doc.prefab_hash:
            lines.extend([f"**Prefab Hash**: `{doc.prefab_hash}`", ""])

        if doc.power_usage:
            lines.extend([f"**Power Usage**: {doc.power_usage}W", ""])

        if doc.readable_logic or doc.writable_logic:
            lines.append("## Logic Types")
            lines.append("")

            if doc.readable_logic:
                lines.append("### Readable")
                lines.append("")
                lines.append("| Logic Type | Description |")
                lines.append("|------------|-------------|")
                for entry in doc.readable_logic:
                    lines.append(f"| {entry['name']} | {entry.get('description', '')} |")
                lines.append("")

            if doc.writable_logic:
                lines.append("### Writable")
                lines.append("")
                lines.append("| Logic Type | Description |")
                lines.append("|------------|-------------|")
                for entry in doc.writable_logic:
                    lines.append(f"| {entry['name']} | {entry.get('description', '')} |")
                lines.append("")

        if doc.slots:
            lines.append("## Slots")
            lines.append("")
            lines.append("| Slot | Type | Purpose |")
            lines.append("|------|------|---------|")
            for slot in doc.slots:
                lines.append(
                    f"| {slot.get('index', '')} | {slot.get('type', '')} | "
                    f"{slot.get('purpose', '')} |"
                )
            lines.append("")

        # Add example
        lines.extend(
            [
                "## IC10 Example",
                "",
                "```ic10",
                f"alias device d0  # {doc.name}",
            ]
        )

        if doc.readable_logic:
            first_readable = doc.readable_logic[0]["name"]
            lines.append(f"l r0 device {first_readable}")

        if doc.writable_logic:
            first_writable = doc.writable_logic[0]["name"]
            lines.append(f"s device {first_writable} 1")

        lines.extend(["```", ""])

        return "\n".join(lines)


def main():
    """Run the wiki scraper."""
    parser = argparse.ArgumentParser(description="Scrape Stationeers wiki")
    parser.add_argument(
        "--target",
        choices=["reference", "devices", "all"],
        default="all",
        help="What to scrape",
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear cached pages before scraping",
    )
    args = parser.parse_args()

    scraper = WikiScraper()

    if args.clear_cache:
        import shutil
        if scraper.cache_dir.exists():
            shutil.rmtree(scraper.cache_dir)
            console.print("[yellow]Cache cleared[/yellow]")
        scraper.cache_dir.mkdir(exist_ok=True)

    if args.target in ["reference", "all"]:
        console.print("\n[bold blue]Phase 1: IC10 Instructions[/bold blue]")
        instructions = scraper.scrape_ic10_reference()
        if instructions:
            scraper.save_instruction_docs(instructions)
            total = sum(len(docs) for docs in instructions.values())
            console.print(f"\n[green]Saved {total} instructions[/green]")

    if args.target in ["devices", "all"]:
        console.print("\n[bold blue]Phase 2: Device Documentation[/bold blue]")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Scraping devices...", total=len(config.COMMON_DEVICES))

            for device_name in config.COMMON_DEVICES:
                progress.update(task, description=f"Scraping: {device_name}")
                doc = scraper.scrape_device(device_name)
                if doc:
                    scraper.save_device_doc(doc)
                progress.advance(task)

        console.print(f"\n[green]Processed {len(config.COMMON_DEVICES)} devices[/green]")

    console.print("\n[bold green]Scraping complete![/bold green]")


if __name__ == "__main__":
    main()
