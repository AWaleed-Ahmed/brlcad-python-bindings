## BRL-CAD Package Core Module (brlcad/)

This directory houses the internal library package logic and foreign-function bindings wrapper code for the BRL-CAD Python integration layer.

## Directory Architecture

```text
brlcad/
├── docs/                 # Technical documentation and markdown notes
├── __init__.py           # Package entry point; exposes public clean interfaces
├── _bindings.py          # Low-level ctypes dynamic C-linker engine (loads libbrlcad.so)
├── Object.py             # Base geometry structure definition properties
├── Arb8.py               # Explicit 8-vertex polyhedral solid primitive support
├── ConstDatabase.py      # Main read-only structural file database bridge class
├── Database.py           # Mutable/Core database base tracking logic
├── FileDatabase.py       # Local file storage system interaction subclass
└── MemoryDatabase.py     # High-speed air-gapped virtual database in-RAM subclass