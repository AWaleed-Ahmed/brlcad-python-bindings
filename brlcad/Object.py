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
from .Handle import Handle

class Object(Handle):
    """Base class for all BRL-CAD geometric primitives."""
    
    def __init__(self, handle=None, owned=True):
        super().__init__(handle=handle, owned=owned)

    def set_name(self, name: str):
        """Sets the structural database lookup name key for this shape."""
        if not self._handle:
            return 
        c_name = ctypes.c_char_p(name.encode('utf-8'))
        _lib.BrlObjectSetName(self._handle, c_name)
        
    def is_valid(self):
        """Returns True if the geometric primitive is valid."""
        return _lib.BrlObjectIsValid(self._handle) == 1

    def get_type(self):
        """Returns the core primitive engine type string."""
        type_str = _lib.BrlObjectType(self._handle)
        return type_str.decode('utf-8') if type_str else ""
