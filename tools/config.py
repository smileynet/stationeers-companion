"""Configuration for Stationeers wiki scraper."""

from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
EXAMPLES_DIR = PROJECT_ROOT / "examples"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"

# Wiki configuration
WIKI_BASE_URL = "https://stationeers-wiki.com"
REQUEST_DELAY = 1.5  # seconds between requests
USER_AGENT = "StationeersCompanion/1.0 (IC10 reference scraper)"

# IC10 instruction categories
INSTRUCTION_CATEGORIES = {
    "math": [
        "add",
        "sub",
        "mul",
        "div",
        "mod",
        "abs",
        "ceil",
        "floor",
        "round",
        "trunc",
        "sqrt",
        "exp",
        "log",
        "pow",
        "sin",
        "cos",
        "tan",
        "asin",
        "acos",
        "atan",
        "atan2",
        "min",
        "max",
        "rand",
    ],
    "logic": [
        "l",
        "s",
        "ls",
        "ss",
        "lr",
        "sr",
        "ld",
        "sd",
    ],
    "batch": [
        "lb",
        "sb",
        "lbn",
        "sbn",
        "lbs",
        "sbs",
        "lbns",
        "sbns",
    ],
    "comparison": [
        "seq",
        "sne",
        "sgt",
        "slt",
        "sge",
        "sle",
        "seqz",
        "snez",
        "sgtz",
        "sltz",
        "sgez",
        "slez",
        "sap",
        "sna",
        "sapz",
        "snaz",
        "sdse",
        "sdns",
        "select",
    ],
    "branching": [
        "j",
        "jr",
        "jal",
        "beq",
        "bne",
        "bgt",
        "blt",
        "bge",
        "ble",
        "beqz",
        "bnez",
        "bgtz",
        "bltz",
        "bgez",
        "blez",
        "beqal",
        "bneal",
        "bgtal",
        "bltal",
        "bgeal",
        "bleal",
        "beqzal",
        "bnezal",
        "bgtzal",
        "bltzal",
        "bgezal",
        "blezal",
        "bap",
        "bna",
        "bapz",
        "bnaz",
        "bapal",
        "bnaal",
        "bdse",
        "bdns",
        "bdseal",
        "bdnsal",
        "brap",
        "brna",
        "breq",
        "brne",
        "brgt",
        "brlt",
        "brge",
        "brle",
        "breqz",
        "brnez",
        "brgtz",
        "brltz",
        "brgez",
        "brlez",
        "brdse",
        "brdns",
    ],
    "bitwise": [
        "and",
        "or",
        "xor",
        "nor",
        "not",
        "sll",
        "srl",
        "sla",
        "sra",
    ],
    "stack": [
        "push",
        "pop",
        "peek",
        "poke",
        "get",
        "put",
        "getd",
        "putd",
    ],
    "utility": [
        "alias",
        "define",
        "move",
        "mv",  # alias for move
        "yield",
        "sleep",
        "hcf",
        "label",
    ],
}

# All instructions flattened
ALL_INSTRUCTIONS = [
    instr for category in INSTRUCTION_CATEGORIES.values() for instr in category
]

# Common devices to scrape
COMMON_DEVICES = [
    # Atmospheric
    "Active Vent",
    "Passive Vent",
    "Volume Pump",
    "Turbo Volume Pump",
    "Gas Sensor",
    "Pipe Analyzer",
    "Filtration",
    "Air Conditioner",
    # Power
    "Solar Panel",
    "Solar Panel (Tracking)",
    "Battery",
    "Battery (Large)",
    "APC",
    "Transformer (Small)",
    "Solid Fuel Generator",
    "Gas Fuel Generator",
    # Logic
    "IC Housing",
    "IC Housing (10 Slot)",
    "Logic Memory",
    "Logic I/O",
    "Logic Switch",
    "Logic Reader",
    "Logic Writer",
    # Fabrication
    "Furnace",
    "Arc Furnace",
    "Centrifuge",
    "Electronics Printer",
    "Hydraulic Pipe Bender",
    "Autolathe",
    # Doors/Airlocks
    "Door",
    "Airlock",
    "Airlock Gate",
    # Sensors
    "Daylight Sensor",
    "Motion Sensor",
    "Occupancy Sensor",
    # Other
    "Console",
    "Kit (Lights)",
    "Dial",
    "Lever",
    "Button",
]

# Output file structure
INSTRUCTION_OUTPUT = DOCS_DIR / "reference" / "instructions"
DEVICE_OUTPUT = DOCS_DIR / "devices"

# GitHub configuration
GITHUB_API_BASE = "https://api.github.com"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com"

# Steam Workshop configuration
STEAM_APPID = 544550  # Stationeers game AppID
STEAM_WORKSHOP_URL = "https://steamcommunity.com/sharedfiles/filedetails"
STEAM_SEARCH_URL = "https://steamcommunity.com/workshop/browse"
STEAM_CACHE_DIR = PROJECT_ROOT / ".cache" / "steam"

# Target repositories for IC10 examples
GITHUB_REPOS = [
    # Primary sources (currently scraped)
    "jhillacre/stationeers-scripts",
    "Zappes/Stationeers",
    # Additional repositories
    "Xon/stationeers-ic-scripts",
    "drclaw1188/stationeers_ic10",
    "FHannes/StationeersScripts",
    "SnorreSelmer/stationeers_ic10",
    "Flow86/stationeers-ic-scripts",
    "bryon82/Stationeers-IC10-Scripts",
    "kogratte/Stationeers.IC",
]

# Keywords for categorization
CATEGORY_KEYWORDS = {
    "atmosphere": [
        "pressure",
        "vent",
        "pump",
        "gas",
        "oxygen",
        "nitrogen",
        "temperature",
        "temp",
        "climate",
        "air",
        "atmosphere",
        "atmos",
        "filtration",
        "filter",
        "conditioner",
        "ac",
        "hvac",
    ],
    "power": [
        "solar",
        "battery",
        "power",
        "generator",
        "energy",
        "watt",
        "apc",
        "transformer",
        "charge",
        "daylight",
        "sun",
    ],
    "airlocks": [
        "airlock",
        "door",
        "cycle",
        "depressur",
        "pressur",
        "lock",
        "gate",
        "hatch",
        "chamber",
    ],
    "patterns": [
        "pid",
        "controller",
        "hysteresis",
        "state",
        "machine",
        "loop",
        "timer",
        "counter",
        "toggle",
        "latch",
        "debounce",
    ],
    "rocketry": [
        "rocket",
        "orbital",
        "atmospheric",
        "flight",
        "thruster",
        "engine",
        "launch",
        "space",
        "trading",
        "shuttle",
    ],
}

# Example output directory
EXAMPLES_OUTPUT = EXAMPLES_DIR

# =============================================================================
# IC10 Validator Configuration
# =============================================================================

# Grammar path for tree-sitter-ic10
GRAMMAR_DIR = PROJECT_ROOT / "tools" / "grammars"
GRAMMAR_PATH = GRAMMAR_DIR / "tree-sitter-ic10.so"

# IC10 hard limits (from Stationeers game)
MAX_LINES = 128
MAX_LINE_LENGTH = 90
MAX_CODE_SIZE = 4096  # bytes

# Valid registers
VALID_REGISTERS = [f"r{i}" for i in range(16)] + ["ra", "sp"]

# Valid device ports
VALID_DEVICES = [f"d{i}" for i in range(6)] + ["db", "dr"]

# Instructions that don't require yield in loops (they pause execution)
YIELD_INSTRUCTIONS = {"yield", "sleep"}

# Instructions that can branch (for loop detection)
BRANCH_INSTRUCTIONS = {
    "j",
    "jr",
    "jal",
    "beq",
    "bne",
    "bgt",
    "blt",
    "bge",
    "ble",
    "beqz",
    "bnez",
    "bgtz",
    "bltz",
    "bgez",
    "blez",
    "beqal",
    "bneal",
    "bgtal",
    "bltal",
    "bgeal",
    "bleal",
    "bap",
    "bna",
    "bapz",
    "bnaz",
    "bdse",
    "bdns",
    "bdseal",
    "bdnsal",
    "brap",
    "brna",
    "breq",
    "brne",
    "brgt",
    "brlt",
    "brge",
    "brle",
}

# Unconditional jump instructions (for unreachable code detection)
UNCONDITIONAL_JUMPS = {"j", "jr", "jal"}
