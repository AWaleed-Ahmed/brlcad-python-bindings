#                       C O N E . P Y
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
# @file Cone.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the Cone.cpp
#

import ctypes
from ._bindings import _lib
from .Object import Object

class Cone(Object):
    """Cone primitive tracking container."""

    def __init__(self, handle=None, owned=True):
        if handle is None:
            handle = _lib.BrlNewCone()
        super().__init__(handle=handle, owned=owned)

    @classmethod
    def create_truncated_general(cls, base, height, semi_axis_a, semi_axis_b, ratio_c_to_a, ratio_d_to_b):
        """Creates a truncated general cone primitive."""
        handle = _lib.BrlNewConeAsTruncatedGeneralCone(
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(ratio_c_to_a), float(ratio_d_to_b)
        )
        return cls(handle)

    @classmethod
    def create_truncated_erected(cls, base, height, semi_axis_a, semi_axis_b, scale):
        """Creates a truncated erected cone primitive configuration."""
        handle = _lib.BrlNewConeAsTruncatedErectedCone(
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(scale)
        )
        return cls(handle)

    @classmethod
    def create_right_elliptical_cylinder(cls, base, height, semi_axis_a, semi_axis_b):
        """Creates a right elliptical cylinder primitive context."""
        handle = _lib.BrlNewConeAsRightEllipticalCylinder(
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2])
        )
        return cls(handle)

    @classmethod
    def create_truncated_right_circular(cls, base, height, radius_base, radius_top):
        """Creates a truncated right circular cone primitive."""
        handle = _lib.BrlNewConeAsTruncatedRightCircularCone(
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(radius_base), float(radius_top)
        )
        return cls(handle)

    @classmethod
    def create_right_circular_cylinder(cls, base, height, radius):
        """Creates a uniform right circular cylinder primitive configuration."""
        handle = _lib.BrlNewConeAsRightCircularCylinder(
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(radius)
        )
        return cls(handle)

    def get_base_point(self):
        """Returns the base reference point pointer mapping address."""
        return _lib.BrlConeBasePoint(self._handle)

    def get_height(self):
        """Returns the height vector pointer mapping address."""
        return _lib.BrlConeHeight(self._handle)

    def get_semi_principal_axis(self, index):
        """Returns the specific semi-principal axis vector pointer by index."""
        return _lib.BrlConeSemiPrincipalAxis(self._handle, int(index))

    def set_base_point(self, x, y, z):
        """Sets the raw base reference location coordinates."""
        _lib.BrlConeSetBasePoint(self._handle, float(x), float(y), float(z))

    def set_height(self, x, y, z):
        """Sets the primary vector height coordinates."""
        _lib.BrlConeSetHeight(self._handle, float(x), float(y), float(z))

    def set_semi_principal_axis(self, index, x, y, z):
        """Modifies an orientation axis coordinate trajectory by its index value."""
        _lib.BrlConeSetSemiPrincipalAxis(self._handle, int(index), float(x), float(y), float(z))

    def set_as_truncated_general_cone(self, base, height, semi_axis_a, semi_axis_b, ratio_c, ratio_d):
        """Mutates the primitive structure into a truncated general cone framework."""
        _lib.BrlConeSetAsTruncatedGeneralCone(
            self._handle,
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(ratio_c), float(ratio_d)
        )

    def set_as_truncated_erected_cone(self, base, height, semi_axis_a, semi_axis_b, scale):
        """Mutates the primitive structure into a truncated erected cone framework."""
        _lib.BrlConeSetAsTruncatedErectedCone(
            self._handle,
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2]),
            float(scale)
        )

    def set_as_right_elliptical_cylinder(self, base, height, semi_axis_a, semi_axis_b):
        """Mutates the primitive structure into a right elliptical cylinder configuration."""
        _lib.BrlConeSetAsRightEllipticalCylinder(
            self._handle,
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(semi_axis_a[0]), float(semi_axis_a[1]), float(semi_axis_a[2]),
            float(semi_axis_b[0]), float(semi_axis_b[1]), float(semi_axis_b[2])
        )

    def set_as_truncated_right_circular_cone(self, base, height, radius_base, radius_top):
        """Mutates the primitive structure into a truncated right circular cone framework."""
        _lib.BrlConeSetAsTruncatedRightCircularCone(
            self._handle,
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(radius_base), float(radius_top)
        )

    def set_as_right_circular_cylinder(self, base, height, radius):
        """Mutates the primitive structure into a uniform right circular cylinder framework."""
        _lib.BrlConeSetAsRightCircularCylinder(
            self._handle,
            float(base[0]), float(base[1]), float(base[2]),
            float(height[0]), float(height[1]), float(height[2]),
            float(radius)
        )
