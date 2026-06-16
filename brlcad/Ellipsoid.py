#                       E L L I P S O I D . P Y
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
# @file Ellipsoid.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the Ellipsoid.cpp
#

from ._bindings import _lib
from .Object import Object

class Ellipsoid(Object):
    """Ellipsoid primitive tracking container."""

    def __init__(self, handle=None, owned=True):
        if handle is None:
            handle = _lib.BrlNewEllipsoid()
        super().__init__(handle=handle, owned=owned)

    @classmethod
    def create(cls, center, semi_axis_a, semi_axis_b, semi_axis_c):
        """Creates a general Ellipsoid primitive using center and semi-principal axes."""
        handle = _lib.BrlNewEllipsoidAsGeneralEllipsoid(
            float(center[0]), float(center[1]), float(center[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(semi_axis_c[0]), float(semi_axis_c[1]), float(semi_axis_c[2])
        )
        return cls(handle)

    @classmethod
    def from_ellipsoid1(cls, center, semi_axis, radius):
        """Creates an Ellipsoid1 variant primitive layout using 1 axis and a radius."""
        handle = _lib.BrlNewEllipsoidAsEllipsoid1(
            float(center[0]), float(center[1]), float(center[2]),
            float(semi_axis[0]), float(semi_axis[1]), float(semi_axis[2]),
            float(radius)
        )
        return cls(handle)

    @classmethod
    def sphere(cls, center, radius):
        """Creates an Ellipsoid representing a sphere."""
        handle = _lib.BrlNewEllipsoidAsSphere(
            float(center[0]), float(center[1]), float(center[2]),
            float(radius)
        )
        return cls(handle)

    def get_center(self):
        """Returns the center point wrapper handle of the ellipsoid."""
        return _lib.BrlEllipsoidCenter(self._handle)

    def get_semi_principal_axis(self, index):
        """Returns the specific semi-principal axis vector pointer by index."""
        return _lib.BrlEllipsoidSemiPrincipalAxis(self._handle, int(index))

    def set_center(self, x, y, z):
        """Sets the center point coordinates of the ellipsoid."""
        _lib.BrlEllipsoidSetCenter(self._handle, float(x), float(y), float(z))

    def set_semi_principal_axis(self, index, x, y, z):
        """Modifies a single directional vector axis by its index location."""
        _lib.BrlEllipsoidSetSemiPrincipalAxis(self._handle, int(index), float(x), float(y), float(z))

    def set_as_general_ellipsoid(self, center, semi_axis_a, semi_axis_b, semi_axis_c):
        """Updates geometry footprint values into a general ellipsoid layout configuration."""
        _lib.BrlEllipsoidSetAsGeneralEllipsoid(
            self._handle,
            float(center[0]), float(center[1]), float(center[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(semi_axis_c[0]), float(semi_axis_c[1]), float(semi_axis_c[2])
        )

    def set_as_ellipsoid1(self, center, semi_axis, radius):
        """Updates geometry footprint values into an Ellipsoid1 subvariant layout."""
        _lib.BrlEllipsoidSetAsEllipsoid1(
            self._handle,
            float(center[0]), float(center[1]), float(center[2]),
            float(semi_axis[0]), float(semi_axis[1]), float(semi_axis[2]),
            float(radius)
        )

    def set_focals(self, focal_a, focal_b, major_axis_length):
        """Sets the geometry properties via focal parameters and major axis length."""
        _lib.BrlEllipsoidSetFocals(
            self._handle,
            float(focal_a[0]), float(focal_a[1]), float(focal_a[2]),
            float(focal_b[0]), float(focal_b[1]), float(focal_b[2]),
            float(major_axis_length)
        )

    def set_sphere(self, x, y, z, radius):
        """Mutates the internal object memory context to hold uniform spherical properties."""
        _lib.BrlEllipsoidSetSphere(self._handle, float(x), float(y), float(z), float(radius))
