#                       C O N S T D A T A B A S E . P Y
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
# @file ConstDatabase.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the ConstDatabase.cpp


import os
import ctypes
from ._bindings import _lib

class ConstDatabase:
    """Object-oriented Python interface for the BRL-CAD ConstDatabase."""
    
    def __init__(self):
        self._handle = _lib.BrlNewConstDatabase()
        if not self._handle:
            self._handle = None

    def Load(self, file_name: str) -> bool:
        """Loads a BRL-CAD database file using the existing handle."""
        if not self._handle:
            self._handle = _lib.BrlNewConstDatabase()
            if not self._handle:
                return False
        
        if not os.path.exists(file_name):
            return False
        c_file = ctypes.c_char_p(file_name.encode('utf-8'))
        status = _lib.BrlConstDatabaseLoad(self._handle, c_file)
        
        if status != 0:
            self.Close()
            return False
            
        return True
        
    def Close(self):
        """Explicitly closes the database and frees C++ memory immediately."""
        if hasattr(self, '_handle') and self._handle is not None:
            _lib.BrlDeleteHandle(self._handle)
            self._handle = None
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
        
    def Title(self) -> str:
        """Extracts and decodes the database internal title header."""
        if not self._handle:
            return ""
        
        raw_ptr = _lib.BrlConstDatabaseTitle(self._handle)
        return raw_ptr.decode('utf-8') if raw_ptr else ""

    def __del__(self):
        self.Close()