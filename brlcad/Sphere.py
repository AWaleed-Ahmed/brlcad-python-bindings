#                       S P H E R E . P Y
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
# @file Sphere.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the Sphere.cpp
#

from ._bindings import _lib
from .Object import Object

class Sphere(Object):
    """Sphere primitive tracking container."""

    def __init__(self, handle=None, owned=True):
        if handle is None:
            handle = _lib.BrlNewSphere()
        super().__init__(handle=handle, owned=owned)

    @classmethod
    def create(cls, center, radius):
        """Creates an initialized Sphere primitive using center coordinates and radius."""
        handle = _lib.BrlNewSphereAsSphere(
            float(center[0]), float(center[1]), float(center[2]),
            float(radius)
        )
        return cls(handle)

    def get_center(self):
        """Returns the center point wrapper handle address of the sphere."""
        return _lib.BrlSphereCenter(self._handle)

    def get_radius(self):
        """Returns the radius of the sphere."""
        return _lib.BrlSphereRadius(self._handle)

    def set_center(self, x, y, z):
        """Sets the center point coordinates of the sphere."""
        _lib.BrlSphereSetCenter(self._handle, float(x), float(y), float(z))

    def set_radius(self, radius):
        """Sets the radius of the sphere."""
        _lib.BrlSphereSetRadius(self._handle, float(radius))

    def set_sphere_properties(self, center, radius):
        """Mutates the complete internal object context properties in one pass."""
        _lib.BrlSphereSet(
            self._handle,
            float(center[0]), float(center[1]), float(center[2]),
            float(radius)
        )
