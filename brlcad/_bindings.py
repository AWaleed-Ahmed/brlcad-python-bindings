#                       _ B I N D I N G S . P Y
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
# @file _bindings.py
#
# BRL-CAD core simplified Python interface:
#       includes all the ctypes for Python Interface
#
 

import ctypes


_lib = ctypes.CDLL("libbrlcad.so")


# Destructor Lifecycle Binding


_lib.BrlDeleteHandle.restype = None
_lib.BrlDeleteHandle.argtypes = [ctypes.c_void_p]


# Database Function Signatures


_lib.BrlNewConstDatabase.restype = ctypes.c_void_p
_lib.BrlNewConstDatabase.argtypes = []

_lib.BrlNewFileDatabase.restype = ctypes.c_void_p
_lib.BrlNewFileDatabase.argtypes = []

_lib.BrlNewMemoryDatabase.restype = ctypes.c_void_p
_lib.BrlNewMemoryDatabase.argtypes = []

_lib.BrlConstDatabaseLoad.restype = ctypes.c_int
_lib.BrlConstDatabaseLoad.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabaseTitle.restype = ctypes.c_char_p
_lib.BrlConstDatabaseTitle.argtypes = [ctypes.c_void_p]

_lib.BrlDatabaseSetTitle.restype = None
_lib.BrlDatabaseSetTitle.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabasePlot.restype = None
_lib.BrlConstDatabasePlot.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

_lib.BrlConstDatabaseGet.restype = ctypes.c_void_p
_lib.BrlConstDatabaseGet.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabaseFacetize.restype = ctypes.c_void_p
_lib.BrlConstDatabaseFacetize.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabaseSelect.restype = None
_lib.BrlConstDatabaseSelect.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

_lib.BrlConstDatabaseUnSelectAll.restype = None
_lib.BrlConstDatabaseUnSelectAll.argtypes = [ctypes.c_void_p]

_lib.BrlConstDatabaseSelectionIsEmpty.restype = ctypes.c_int
_lib.BrlConstDatabaseSelectionIsEmpty.argtypes = [ctypes.c_void_p]

_lib.BrlConstDatabaseBoundingBoxMinima.restype = None
_lib.BrlConstDatabaseBoundingBoxMinima.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

_lib.BrlConstDatabaseBoundingBoxMaxima.restype = None
_lib.BrlConstDatabaseBoundingBoxMaxima.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]


# Database TopObjectIterator Function Signatures


_lib.BrlConstDatabaseFirstTopObject.restype = ctypes.c_void_p
_lib.BrlConstDatabaseFirstTopObject.argtypes = [ctypes.c_void_p]

_lib.BrlTopObjectIteratorGood.restype = ctypes.c_int
_lib.BrlTopObjectIteratorGood.argtypes = [ctypes.c_void_p]

_lib.BrlTopObjectIteratorNext.restype = None
_lib.BrlTopObjectIteratorNext.argtypes = [ctypes.c_void_p]

_lib.BrlTopObjectIteratorName.restype = ctypes.c_char_p
_lib.BrlTopObjectIteratorName.argtypes = [ctypes.c_void_p]

_lib.BrlDeleteTopObjectIterator.restype = None
_lib.BrlDeleteTopObjectIterator.argtypes = [ctypes.c_void_p]


# Geometry Function Signatures


_lib.BrlNewArb8From2Points.restype = ctypes.c_void_p
_lib.BrlNewArb8From2Points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]

_lib.BrlNewArb8From8Points.restype = ctypes.c_void_p
_lib.BrlNewArb8From8Points.argtypes = [ctypes.c_double] * 24

_lib.BrlObjectSetName.restype = None
_lib.BrlObjectSetName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]


# VectorList Function Signatures


_lib.BrlNewVectorList.restype = ctypes.c_void_p
_lib.BrlNewVectorList.argtypes = []

_lib.BrlVectorListClear.restype = None
_lib.BrlVectorListClear.argtypes = [ctypes.c_void_p]