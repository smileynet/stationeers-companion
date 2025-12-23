# Stationeers Companion

Personal toolkit for Stationeers IC10 programming with Claude AI integration.

## Features

- **IC10 Reference Documentation** - Complete instruction syntax and device properties
- **Code Examples** - Working scripts for common automation tasks
- **Claude Integration** - AI-powered code generation, debugging, and optimization
- **Game Knowledge Base** - Items, crafting, and systems reference

## Quick Start

Ask Claude to help with IC10 programming:

```
"Create an IC10 script that controls vents to maintain 101 kPa pressure"
"What does this IC10 code do? [paste code]"
"My pressure regulator isn't working, help me debug it"
"How do I read the temperature from a gas sensor?"
```

Claude will automatically use the appropriate skill based on your request.

## Project Structure

```
docs/                    IC10 reference documentation
  reference/             Instruction syntax and usage
  devices/               Device properties and logic values
examples/                Working IC10 code examples
  atmosphere/            Pressure, temperature control
  power/                 Solar, battery management
  airlocks/              Airlock cycling
knowledge/               Game knowledge base
tools/                   Python scraping utilities
outputs/                 Generated code output
```

## Skills

Claude automatically invokes these skills:

| Skill | Triggers When |
|-------|---------------|
| ic-generate | You ask to create IC10 code |
| ic-explain | You paste code and ask what it does |
| ic-debug | Your IC10 code isn't working |
| ic-optimize | You want to improve code efficiency |
| ic-lookup | You ask about device properties or instructions |
| ic-example | You ask for example code or patterns |

## IC10 Quick Reference

### Code Template

```ic10
# Description: [What this code does]
# Devices: d0=[type], d1=[type]

alias sensor d0
alias actuator d1
define TARGET 101.325

main:
l r0 sensor Pressure
sgt r1 r0 TARGET
s actuator On r1
yield
j main
```

### Key Constraints

- 128 lines max, 90 chars/line
- 16 registers (r0-r15) + ra, sp
- 6 device ports (d0-d5) + db (self)
- Always use `yield` in loops

## Development

### Scraping Tools

```bash
# Install dependencies
uv sync

# Scrape wiki content
uv run python -m tools.wiki_scraper --target reference
uv run python -m tools.wiki_scraper --target devices

# Collect GitHub examples
uv run python -m tools.github_scraper
```

## Resources

- [Stationeers Wiki - IC10](https://stationeers-wiki.com/IC10)
- [IC10 Instructions Reference](https://stationeers-wiki.com/IC10/instructions)
- [IC10 Simulator](https://ic10.dev/)
- [IC10 Emulator](https://ic10emu.dev/)
