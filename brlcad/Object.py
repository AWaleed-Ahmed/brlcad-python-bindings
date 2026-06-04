#                       O B J E C T . P Y
#  BRL-CAD
#
# Copyright (c) 2026 United States Government as represented by
# the U.S. Army Research Laboratory.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this file; see the file named COPYING for more
# information.
#
# @file Object.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the Object.cpp


import ctypes
from ._bindings import _lib

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