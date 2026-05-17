"""ctypes-based bridge loader and lightweight wrapper for BRL-CAD MOOSE."""
from __future__ import annotations

import os
import ctypes
from typing import Optional, Sequence

# Default path pointing to the updated main-line library target
LIB_PATH_DEFAULT = "/home/home/brlcad-dev/moose_install/lib/libbrlcad.so"


class LibraryLoadError(RuntimeError):
    pass


class Bindings:
    """Loader + registry for BRL-CAD C bridge functions using ctypes."""

    def __init__(self, lib_path: Optional[str] = None) -> None:
        self.lib_path = (
            lib_path
            or os.environ.get("BRLCAD_LIB_PATH")
            or LIB_PATH_DEFAULT
        )
        self.lib: Optional[ctypes.CDLL] = None
        self._registry = {}
        
        # Load the binary
        self._load_library()
        
        # Register the API functions immediately on initialization
        self.register_core_api()

    def _load_library(self) -> None:
        try:
            self.lib = ctypes.CDLL(self.lib_path)
        except OSError as exc:
            raise LibraryLoadError(
                f"Could not load library at {self.lib_path}: {exc}"
            )

    def register_function(
        self,
        name: str,
        argtypes: Optional[Sequence] = None,
        restype: Optional = ctypes.c_int,
    ):
        """Resolve and cache a function from the loaded library."""
        if not self.lib:
            raise LibraryLoadError("Library not loaded")
        try:
            func = getattr(self.lib, name)
        except AttributeError:
            raise AttributeError(f"Function '{name}' not found in {self.lib_path}")

        if argtypes is not None:
            func.argtypes = list(argtypes)
        func.restype = restype
        self._registry[name] = func
        return func

    # 2. API Registration Layer
    def register_core_api(self):
        """Registers the explicit C-Bridge signatures once up front."""
        
        # 1. Constructor: Creates a fresh, empty database handle container
        self.register_function(
            "BrlNewConstDatabase",
            argtypes=[],
            restype=ctypes.c_void_p
        )
        
        # 2. Database Load mapping (Takes the handle pointer AND the filename string)
        self.register_function(
            "BrlConstDatabaseLoad", 
            argtypes=[ctypes.c_void_p, ctypes.c_char_p], # Fixed argtypes layout!
            restype=ctypes.c_int                        # Returns an int status code
        )
        
        # 3. Database Title fetching mapping
        self.register_function(
            "BrlConstDatabaseTitle", 
            argtypes=[ctypes.c_void_p], 
            restype=ctypes.c_char_p
        )
        
        # 4. Memory Release mapping
        self.register_function(
            "BrlDeleteConstDatabase", 
            argtypes=[ctypes.c_void_p], 
            restype=None
        )

    # 3. Clean Python Execution Helpers
    def database_create(self) -> ctypes.c_void_p:
        """Instantiates a fresh container handle pointer via BrlNewConstDatabase."""
        return self._registry["BrlNewConstDatabase"]()

    def database_load(self, db_ptr: ctypes.c_void_p, filename: str) -> int:
        """Loads a .g file configuration into an active pointer allocation."""
        filename_bytes = filename.encode("utf-8")
        return self._registry["BrlConstDatabaseLoad"](db_ptr, filename_bytes)

    def database_get_title(self, db_ptr: ctypes.c_void_p) -> Optional[str]:
        """Fetches the title from a database pointer and decodes it safely."""
        if not db_ptr:
            return None
        raw = self._registry["BrlConstDatabaseTitle"](db_ptr)
        if not raw:
            return None
        return raw.decode("utf-8", errors="replace")

    def database_free(self, db_ptr: ctypes.c_void_p) -> None:
        """Explicitly releases the database resource on the C++ side."""
        if db_ptr:
            self._registry["BrlDeleteConstDatabase"](db_ptr)