"""GitHub scraper for IC10 code examples."""

import argparse
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import requests
from rich.console import Console

from . import config

console = Console()


@dataclass
class IC10Script:
    """An IC10 script from GitHub."""

    name: str
    content: str
    source_url: str
    repo: str
    path: str
    category: str = "patterns"
    description: str = ""
    devices: list[str] = field(default_factory=list)


class GitHubScraper:
    """Scraper for IC10 examples from GitHub repositories."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = config.USER_AGENT
        self.session.headers["Accept"] = "application/vnd.github.v3+json"

    def search_repo_for_ic10(self, repo: str) -> list[dict]:
        """Search a repository for IC10 files."""
        console.print(f"  [cyan]Searching {repo}...[/cyan]")

        # Search for .ic10 files
        results = []

        # Try to get repo contents recursively
        try:
            contents = self._get_repo_contents(repo, "")
            ic10_files = self._find_ic10_files(contents, repo)
            results.extend(ic10_files)
        except Exception as e:
            console.print(f"  [yellow]Warning: {e}[/yellow]")

        # Also try GitHub code search for .ic10 extension
        try:
            search_results = self._search_code(repo, "extension:ic10")
            for item in search_results:
                if item not in results:
                    results.append(item)
        except Exception as e:
            console.print(f"  [dim]Code search unavailable: {e}[/dim]")

        return results

    def _get_repo_contents(self, repo: str, path: str, depth: int = 0) -> list[dict]:
        """Get contents of a repository path recursively."""
        if depth > 3:  # Limit recursion depth
            return []

        url = f"{config.GITHUB_API_BASE}/repos/{repo}/contents/{path}"

        try:
            response = self.session.get(url, timeout=30)
            if response.status_code == 404:
                return []
            response.raise_for_status()
            time.sleep(0.5)  # Rate limiting

            contents = response.json()
            if not isinstance(contents, list):
                contents = [contents]

            results = []
            for item in contents:
                if item["type"] == "file":
                    results.append(item)
                elif item["type"] == "dir" and depth < 3:
                    # Recurse into directories
                    sub_contents = self._get_repo_contents(
                        repo, item["path"], depth + 1
                    )
                    results.extend(sub_contents)

            return results
        except requests.RequestException:
            return []

    def _find_ic10_files(self, contents: list[dict], repo: str) -> list[dict]:
        """Filter contents for IC10 files."""
        ic10_files = []
        for item in contents:
            name = item.get("name", "").lower()
            if name.endswith(".ic10") or name.endswith(".mips"):
                ic10_files.append(
                    {
                        "name": item["name"],
                        "path": item["path"],
                        "download_url": item.get("download_url"),
                        "html_url": item.get("html_url"),
                        "repo": repo,
                    }
                )
        return ic10_files

    def _search_code(self, repo: str, query: str) -> list[dict]:
        """Search for code in a repository."""
        url = f"{config.GITHUB_API_BASE}/search/code"
        params = {"q": f"{query} repo:{repo}"}

        try:
            response = self.session.get(url, params=params, timeout=30)
            if response.status_code == 403:
                # Rate limited or requires auth
                return []
            response.raise_for_status()
            time.sleep(1)  # Rate limiting for search API

            data = response.json()
            results = []
            for item in data.get("items", []):
                results.append(
                    {
                        "name": item["name"],
                        "path": item["path"],
                        "html_url": item["html_url"],
                        "repo": repo,
                    }
                )
            return results
        except requests.RequestException:
            return []

    def download_script(self, file_info: dict) -> Optional[IC10Script]:
        """Download and parse an IC10 script."""
        repo = file_info["repo"]
        path = file_info["path"]
        name = file_info["name"]

        # Construct raw URL
        download_url = file_info.get("download_url")
        if not download_url:
            download_url = f"{config.GITHUB_RAW_BASE}/{repo}/main/{path}"

        try:
            response = self.session.get(download_url, timeout=30)
            if response.status_code == 404:
                # Try master branch
                download_url = f"{config.GITHUB_RAW_BASE}/{repo}/master/{path}"
                response = self.session.get(download_url, timeout=30)

            response.raise_for_status()
            content = response.text
            time.sleep(0.3)

            # Parse and categorize
            script = IC10Script(
                name=Path(name).stem,
                content=content,
                source_url=file_info.get("html_url", download_url),
                repo=repo,
                path=path,
            )

            self._analyze_script(script)
            return script

        except requests.RequestException as e:
            console.print(f"  [red]Failed to download {name}: {e}[/red]")
            return None

    def _analyze_script(self, script: IC10Script) -> None:
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
                    score += 2  # Name match is stronger signal
            if score > 0:
                category_scores[category] = score

        if category_scores:
            script.category = max(category_scores, key=category_scores.get)

        # Extract description from comments
        lines = script.content.split("\n")
        description_lines = []
        for line in lines[:20]:  # Check first 20 lines
            line = line.strip()
            if line.startswith("#"):
                comment = line[1:].strip()
                # Skip device aliases and empty comments
                if comment and not comment.startswith("=") and len(comment) > 3:
                    description_lines.append(comment)
            elif line and not line.startswith("#"):
                break  # Stop at first non-comment line

        if description_lines:
            script.description = " ".join(description_lines[:3])

        # Extract device aliases
        device_pattern = re.compile(r"alias\s+(\w+)\s+(d[0-5b])", re.IGNORECASE)
        for match in device_pattern.finditer(script.content):
            alias_name = match.group(1)
            device_port = match.group(2)
            script.devices.append(f"{device_port} = {alias_name}")

    def collect_all_examples(self) -> list[IC10Script]:
        """Collect examples from all configured repositories."""
        all_scripts: list[IC10Script] = []

        console.print("[bold]Searching for IC10 examples...[/bold]")

        for repo in config.GITHUB_REPOS:
            files = self.search_repo_for_ic10(repo)
            console.print(f"  Found {len(files)} IC10 files in {repo}")

            for file_info in files:
                script = self.download_script(file_info)
                if script:
                    all_scripts.append(script)
                    console.print(
                        f"    [green]✓[/green] {script.name} → {script.category}"
                    )

        return all_scripts

    def save_examples(self, scripts: list[IC10Script]) -> None:
        """Save examples organized by category."""
        console.print(f"\n[bold]Saving to {config.EXAMPLES_OUTPUT}[/bold]")

        # Group by category
        by_category: dict[str, list[IC10Script]] = {}
        for script in scripts:
            if script.category not in by_category:
                by_category[script.category] = []
            by_category[script.category].append(script)

        # Save each category
        for category, cat_scripts in by_category.items():
            category_dir = config.EXAMPLES_OUTPUT / category
            category_dir.mkdir(parents=True, exist_ok=True)

            for script in cat_scripts:
                self._save_script(script, category_dir)

            # Create README for category
            self._create_category_readme(category, cat_scripts, category_dir)

        # Create main index
        self._create_examples_index(by_category)

    def _save_script(self, script: IC10Script, category_dir: Path) -> None:
        """Save a script with proper header."""
        # Clean filename
        filename = re.sub(r"[^a-zA-Z0-9_-]", "-", script.name.lower())
        filename = re.sub(r"-+", "-", filename).strip("-")
        filepath = category_dir / f"{filename}.ic10"

        # Check if content already has a good header
        has_header = script.content.strip().startswith("#")

        if has_header:
            # Just add source attribution
            content = f"# Source: {script.source_url}\n"
            content += f"# Repository: {script.repo}\n"
            content += "#\n"
            content += script.content
        else:
            # Create full header
            content = self._generate_header(script)
            content += script.content

        filepath.write_text(content)
        console.print(f"  Saved: {category_dir.name}/{filepath.name}")

    def _generate_header(self, script: IC10Script) -> str:
        """Generate a header for a script."""
        lines = [
            "# " + "=" * 50,
            f"# {script.name}",
            "# " + "=" * 50,
            f"# Source: {script.source_url}",
            f"# Repository: {script.repo}",
            f"# Category: {script.category}",
            "#",
        ]

        if script.description:
            lines.append(f"# Description: {script.description}")
            lines.append("#")

        if script.devices:
            lines.append("# Devices:")
            for device in script.devices:
                lines.append(f"#   {device}")
            lines.append("#")

        lines.append("# " + "=" * 50)
        lines.append("")

        return "\n".join(lines)

    def _create_category_readme(
        self, category: str, scripts: list[IC10Script], category_dir: Path
    ) -> None:
        """Create README for a category."""
        title = category.replace("_", " ").title()

        lines = [
            f"# {title} Examples",
            "",
            f"IC10 code examples for {category} automation in Stationeers.",
            "",
            "## Scripts",
            "",
            "| Script | Description | Devices |",
            "|--------|-------------|---------|",
        ]

        for script in scripts:
            filename = re.sub(r"[^a-zA-Z0-9_-]", "-", script.name.lower())
            filename = re.sub(r"-+", "-", filename).strip("-") + ".ic10"
            desc = (
                script.description[:60] + "..."
                if len(script.description) > 60
                else script.description
            )
            devices = ", ".join(script.devices[:3]) if script.devices else "-"
            lines.append(f"| [{script.name}]({filename}) | {desc or '-'} | {devices} |")

        lines.extend(
            [
                "",
                "## Sources",
                "",
            ]
        )

        repos = set(s.repo for s in scripts)
        for repo in repos:
            lines.append(f"- [github.com/{repo}](https://github.com/{repo})")

        lines.append("")

        (category_dir / "README.md").write_text("\n".join(lines))
        console.print(f"  Saved: {category_dir.name}/README.md")

    def _create_examples_index(self, by_category: dict[str, list[IC10Script]]) -> None:
        """Create main examples index."""
        lines = [
            "# IC10 Code Examples",
            "",
            "Working IC10 code examples for Stationeers automation.",
            "",
            "## Categories",
            "",
        ]

        for category, scripts in sorted(by_category.items()):
            title = category.replace("_", " ").title()
            lines.append(f"### [{title}]({category}/)")
            lines.append("")
            lines.append(f"{len(scripts)} examples")
            lines.append("")

            # List first few scripts
            for script in scripts[:5]:
                lines.append(
                    f"- `{script.name}` - {script.description[:50] or 'IC10 script'}..."
                )
            if len(scripts) > 5:
                lines.append(f"- ... and {len(scripts) - 5} more")
            lines.append("")

        (config.EXAMPLES_OUTPUT / "index.md").write_text("\n".join(lines))
        console.print("  Saved: examples/index.md")


def main():
    """Run the GitHub scraper."""
    parser = argparse.ArgumentParser(description="Collect IC10 examples from GitHub")
    parser.add_argument(
        "--repos",
        nargs="+",
        help="Specific repositories to scrape (owner/repo format)",
    )
    args = parser.parse_args()

    scraper = GitHubScraper()

    if args.repos:
        # Override default repos
        import tools.config as cfg

        cfg.GITHUB_REPOS = args.repos

    scripts = scraper.collect_all_examples()

    if scripts:
        console.print(f"\n[green]Collected {len(scripts)} scripts[/green]")
        scraper.save_examples(scripts)
    else:
        console.print("\n[yellow]No scripts found[/yellow]")

    console.print("\n[bold green]GitHub scraping complete![/bold green]")


if __name__ == "__main__":
    main()
