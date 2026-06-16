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


# ConstDatabase Function Signatures


_lib.BrlConstDatabaseTitle.restype = ctypes.c_char_p
_lib.BrlConstDatabaseTitle.argtypes = [ctypes.c_void_p]

_lib.BrlConstDatabasePlot.restype = None
_lib.BrlConstDatabasePlot.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

_lib.BrlConstDatabaseLoad.restype = ctypes.c_int
_lib.BrlConstDatabaseLoad.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

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

_lib.BrlNewConstDatabase.restype = ctypes.c_void_p
_lib.BrlNewConstDatabase.argtypes = []

# File Database Function Signatures


_lib.BrlNewFileDatabase.restype = ctypes.c_void_p
_lib.BrlNewFileDatabase.argtypes = []

# Memory Database Function Signatures


_lib.BrlNewMemoryDatabase.restype = ctypes.c_void_p
_lib.BrlNewMemoryDatabase.argtypes = []

# Database Function Signatures


_lib.BrlDatabaseSetTitle.restype = None
_lib.BrlDatabaseSetTitle.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

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


# Object Function Signatures

_lib.BrlObjectIsValid.restype = ctypes.c_int
_lib.BrlObjectIsValid.argtypes = [ctypes.c_void_p]

_lib.BrlObjectType.restype = ctypes.c_char_p
_lib.BrlObjectType.argtypes = [ctypes.c_void_p]

_lib.BrlObjectSetName.restype = None
_lib.BrlObjectSetName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

# Arb8 Function Signatures

_lib.BrlNewArb8AsArb4.restype = ctypes.c_void_p
_lib.BrlNewArb8AsArb4.argtypes = [ctypes.c_double] * 6

_lib.BrlNewArb8AsArb8.restype = ctypes.c_void_p
_lib.BrlNewArb8AsArb8.argtypes = [ctypes.c_double] * 24

_lib.BrlNewArb8AsRectengularParallelPiped.restype = ctypes.c_void_p
_lib.BrlNewArb8AsRectengularParallelPiped.argtypes = [ctypes.c_double] * 6

# Ellipsoid Function Signatures
_lib.BrlNewEllipsoid.restype = ctypes.c_void_p
_lib.BrlNewEllipsoid.argtypes = []

_lib.BrlNewEllipsoidAsGeneralEllipsoid.restype = ctypes.c_void_p
_lib.BrlNewEllipsoidAsGeneralEllipsoid.argtypes = [ctypes.c_double] * 12

_lib.BrlNewEllipsoidAsEllipsoid1.restype = ctypes.c_void_p
_lib.BrlNewEllipsoidAsEllipsoid1.argtypes = [ctypes.c_double] * 7

_lib.BrlNewEllipsoidAsSphere.restype = ctypes.c_void_p
_lib.BrlNewEllipsoidAsSphere.argtypes = [ctypes.c_double] * 4

_lib.BrlEllipsoidCenter.restype = ctypes.c_void_p
_lib.BrlEllipsoidCenter.argtypes = [ctypes.c_void_p]

_lib.BrlEllipsoidSetCenter.restype = None
_lib.BrlEllipsoidSetCenter.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlEllipsoidSemiPrincipalAxis.restype = ctypes.c_void_p
_lib.BrlEllipsoidSemiPrincipalAxis.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

_lib.BrlEllipsoidSetSemiPrincipalAxis.restype = None
_lib.BrlEllipsoidSetSemiPrincipalAxis.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlEllipsoidSetFocals.restype = None
_lib.BrlEllipsoidSetFocals.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 7

_lib.BrlEllipsoidSetSphere.restype = None
_lib.BrlEllipsoidSetSphere.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlEllipsoidSetAsGeneralEllipsoid.restype = None
_lib.BrlEllipsoidSetAsGeneralEllipsoid.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 12

_lib.BrlEllipsoidSetAsEllipsoid1.restype = None
_lib.BrlEllipsoidSetAsEllipsoid1.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 7

# Sphere Function Signatures

_lib.BrlNewSphere.restype = ctypes.c_void_p
_lib.BrlNewSphere.argtypes = []

_lib.BrlNewSphereAsSphere.restype = ctypes.c_void_p
_lib.BrlNewSphereAsSphere.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlSphereRadius.restype = ctypes.c_double
_lib.BrlSphereRadius.argtypes = [ctypes.c_void_p]

_lib.BrlSphereSetRadius.restype = None
_lib.BrlSphereSetRadius.argtypes = [ctypes.c_void_p, ctypes.c_double]

_lib.BrlSphereCenter.restype = ctypes.c_void_p
_lib.BrlSphereCenter.argtypes = [ctypes.c_void_p]

_lib.BrlSphereSetCenter.restype = None
_lib.BrlSphereSetCenter.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlSphereSet.restype = None
_lib.BrlSphereSet.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Cone Function Signatures 

_lib.BrlNewCone.restype = ctypes.c_void_p
_lib.BrlNewCone.argtypes = []

_lib.BrlNewConeAsTruncatedGeneralCone.restype = ctypes.c_void_p
_lib.BrlNewConeAsTruncatedGeneralCone.argtypes = [ctypes.c_double] * 14

_lib.BrlNewConeAsTruncatedErectedCone.restype = ctypes.c_void_p
_lib.BrlNewConeAsTruncatedErectedCone.argtypes = [ctypes.c_double] * 13

_lib.BrlNewConeAsRightEllipticalCylinder.restype = ctypes.c_void_p
_lib.BrlNewConeAsRightEllipticalCylinder.argtypes = [ctypes.c_double] * 12

_lib.BrlNewConeAsTruncatedRightCircularCone.restype = ctypes.c_void_p
_lib.BrlNewConeAsTruncatedRightCircularCone.argtypes = [ctypes.c_double] * 8

_lib.BrlNewConeAsRightCircularCylinder.restype = ctypes.c_void_p
_lib.BrlNewConeAsRightCircularCylinder.argtypes = [ctypes.c_double] * 7

_lib.BrlConeSetAsTruncatedRightCircularCone.restype = None
_lib.BrlConeSetAsTruncatedRightCircularCone.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 8

_lib.BrlConeBasePoint.restype = ctypes.c_void_p
_lib.BrlConeBasePoint.argtypes = [ctypes.c_void_p]

_lib.BrlConeSetAsTruncatedGeneralCone.restype = None
_lib.BrlConeSetAsTruncatedGeneralCone.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 14

_lib.BrlConeSetAsTruncatedErectedCone.restype = None
_lib.BrlConeSetAsTruncatedErectedCone.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 13

_lib.BrlConeSetAsRightEllipticalCylinder.restype = None
_lib.BrlConeSetAsRightEllipticalCylinder.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 12

_lib.BrlConeSetAsRightCircularCylinder.restype = None
_lib.BrlConeSetAsRightCircularCylinder.argtypes = [ctypes.c_void_p] + [ctypes.c_double] * 7

_lib.BrlConeSetBasePoint.restype = None
_lib.BrlConeSetBasePoint.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlConeHeight.restype = ctypes.c_void_p
_lib.BrlConeHeight.argtypes = [ctypes.c_void_p]

_lib.BrlConeSetHeight.restype = None
_lib.BrlConeSetHeight.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double]

_lib.BrlConeSemiPrincipalAxis.restype = ctypes.c_void_p
_lib.BrlConeSemiPrincipalAxis.argtypes = [ctypes.c_void_p, ctypes.c_int]

_lib.BrlConeSetSemiPrincipalAxis.restype = None
_lib.BrlConeSetSemiPrincipalAxis.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]

# VectorList Function Signatures


_lib.BrlNewVectorList.restype = ctypes.c_void_p
_lib.BrlNewVectorList.argtypes = []

_lib.BrlVectorListClear.restype = None
_lib.BrlVectorListClear.argtypes = [ctypes.c_void_p]