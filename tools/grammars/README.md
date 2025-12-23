# IC10 Tree-sitter Grammar

This directory contains the tree-sitter grammar for IC10 parsing.

## Building the Grammar

### Prerequisites

1. **Rust toolchain**: Install from https://rustup.rs/
2. **tree-sitter CLI**: `cargo install tree-sitter-cli`

### Build Steps

```bash
# Clone the grammar repository
git clone https://github.com/Xandaros/tree-sitter-ic10.git
cd tree-sitter-ic10

# Generate parser (creates src/parser.c)
tree-sitter generate

# Build shared library for Python
# Linux:
cc -shared -fPIC -o tree-sitter-ic10.so -I./src src/parser.c

# macOS:
# cc -shared -fPIC -o tree-sitter-ic10.dylib -I./src src/parser.c

# Copy to this directory
cp tree-sitter-ic10.so /path/to/stationeers_companion/tools/grammars/
```

### Alternative: Using py-tree-sitter's build system

```python
from tree_sitter import Language

# Build the library (run once)
Language.build_library(
    'build/ic10.so',
    ['path/to/tree-sitter-ic10']
)
```

## Files

- `tree-sitter-ic10.so` - Compiled grammar (not checked in, build locally)
- `README.md` - This file

## Usage

The grammar is loaded by `tools/ic10_validator.py` for parsing IC10 code.

```python
import tree_sitter

# Load the IC10 language
IC10_LANGUAGE = tree_sitter.Language('tools/grammars/tree-sitter-ic10.so', 'ic10')

# Create parser
parser = tree_sitter.Parser()
parser.set_language(IC10_LANGUAGE)

# Parse code
tree = parser.parse(b"move r0 1\nyield")
```

## License

tree-sitter-ic10 is MIT licensed: https://github.com/Xandaros/tree-sitter-ic10
