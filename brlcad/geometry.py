import ctypes

# Link to your compiled C-bridge library asset
try:
    _lib = ctypes.CDLL("libbrlcad.so")
except OSError as e:
    raise FileNotFoundError("Could not link libbrlcad.so asset framework.") from e

# -------------------------------------------------------------------------
# Define C-Bridge Signatures
# -------------------------------------------------------------------------
_lib.BrlNewArb8From2Points.restype = ctypes.c_void_p
_lib.BrlNewArb8From2Points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]

_lib.BrlNewArb8From8Points.restype = ctypes.c_void_p
_lib.BrlNewArb8From8Points.argtypes = [ctypes.c_double] * 24

_lib.BrlDeleteHandle.restype = None
_lib.BrlDeleteHandle.argtypes = [ctypes.c_void_p]

# The brand-new object manipulation function signature!
_lib.BrlObjectSetName.restype = None
_lib.BrlObjectSetName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]


# -------------------------------------------------------------------------
# Object Hierarchy Porting
# -------------------------------------------------------------------------

class Object:
    """Base class for all BRL-CAD geometric primitives."""
    def __init__(self):
        self._handle = None

    def set_name(self, name: str):
        """Sets the structural database lookup name key for this shape."""
        if not self._handle:
            raise ValueError("Cannot name an unallocated primitive handle.")
        c_name = ctypes.c_char_p(name.encode('utf-8'))
        _lib.BrlObjectSetName(self._handle, c_name)

    def close(self):
        """Releases the underlying primitive allocation safely from memory heap."""
        if hasattr(self, '_handle') and self._handle is not None:
            _lib.BrlDeleteHandle(self._handle)
            self._handle = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()


class Arb8(Object):
    """8-Vertex Arbitrary Polyhedron primitive tracking container."""
    
    @classmethod
    def from_2_points(cls, p1, p2):
        """Creates an aligned bounding box cube from 2 diagonal vertices."""
        instance = cls()
        instance._handle = _lib.BrlNewArb8From2Points(
            p1[0], p1[1], p1[2],
            p2[0], p2[1], p2[2]
        )
        return instance

    @classmethod
    def from_8_points(cls, points_list):
        """Creates an explicit 8-point structural polyhedron wrapper."""
        if len(points_list) != 8 or any(len(p) != 3 for p in points_list):
            raise ValueError("An explicit Arb8 requires exactly 8 points of (X, Y, Z) dimensions.")
        
        # Flatten out 8 coordinates pairs [x1,y1,z1, x2,y2,z2...]
        flat_coords = [float(coord) for point in points_list for coord in point]
        
        instance = cls()
        instance._handle = _lib.BrlNewArb8From8Points(*flat_coords)
        return instance