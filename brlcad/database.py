import ctypes
import os

# Point directly to the compiled C-bridge shared library file
_lib_path = os.path.expanduser("~/brlcad-dev/moose/build/src/libbrlcad.so")
_lib = ctypes.CDLL(_lib_path)

# Configure raw C-Bridge function signatures
_lib.BrlNewConstDatabase.restype = ctypes.c_void_p
_lib.BrlNewConstDatabase.argtypes = []

_lib.BrlDeleteConstDatabase.restype = None
_lib.BrlDeleteConstDatabase.argtypes = [ctypes.c_void_p]

_lib.BrlConstDatabaseLoad.restype = ctypes.c_int
_lib.BrlConstDatabaseLoad.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabaseTitle.restype = ctypes.c_char_p
_lib.BrlConstDatabaseTitle.argtypes = [ctypes.c_void_p]


class ConstDatabase:
    """Object-oriented Python interface for the BRL-CAD ConstDatabase."""
    
    def __init__(self):
        # Instantiate the underlying tracking container in memory
        self._handle = _lib.BrlNewConstDatabase()
        if not self._handle:
            self._handle = None

    def Load(self, file_name: str) -> bool:
        """Loads a BRL-CAD database file using the existing handle."""
        # If the handle was explicitly closed earlier, revive it
        if not self._handle:
            self._handle = _lib.BrlNewConstDatabase()
            if not self._handle:
                return False
        
        # Guard against missing files before passing to C++
        if not os.path.exists(file_name):
            return False
        c_file = ctypes.c_char_p(file_name.encode('utf-8'))
        status = _lib.BrlConstDatabaseLoad(self._handle, c_file)
        
        # If the load failed natively, clean up the handle state
        if status != 0:
            self.Close()
            return False
            
        return True
        
    def Close(self):
        """Explicitly closes the database and frees C++ memory immediately."""
        if hasattr(self, '_handle') and self._handle is not None:
            _lib.BrlDeleteConstDatabase(self._handle)
            self._handle = None  # Clear the state
            
        
    #Python context manager protocol
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close() # Guarantees closing even if the script crashes mid-way
        
    def Title(self) -> str:
        """Extracts and decodes the database internal title header."""
        if not self._handle:
            return ""
        
        raw_ptr = _lib.BrlConstDatabaseTitle(self._handle)
        return raw_ptr.decode('utf-8') if raw_ptr else ""

    def __del__(self):
        # Fallback safety net in case the user forgets to call Close()
        self.Close()