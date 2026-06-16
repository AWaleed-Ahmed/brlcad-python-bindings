#                       A R B 8 . P Y
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
# @file Arb8.py
#
# BRL-CAD core simplified Python interface:
#       Python interface implementation for the Arb8.cpp

 
from ._bindings import _lib
from .Object import Object

class Arb8(Object):
    """8-Vertex Arbitrary Polyhedron primitive tracking container."""
    
    def from_2_points(cls, p1, p2):
        """Creates an Arb4 variant primitive configuration from 2 diagonal bounds."""
        handle = _lib.BrlNewArb8AsArb4(
            float(p1[0]), float(p1[1]), float(p1[2]),
            float(p2[0]), float(p2[1]), float(p2[2])
        )
        return cls(handle)

    def as_rectangular_parallel_piped(cls, p1, p2):
        """Creates a rectangular parallel piped (rpp) primitive form."""
        handle = _lib.BrlNewArb8AsRectengularParallelPiped(
            float(p1[0]), float(p1[1]), float(p1[2]),
            float(p2[0]), float(p2[1]), float(p2[2])
        )
        return cls(handle)

    def from_8_points(cls, points_list):
        """Creates an explicit 8-point structural polyhedron configuration."""
        if len(points_list) != 8 or any(len(p) != 3 for p in points_list):
            raise ValueError("An explicit Arb8 requires exactly 8 points of (X, Y, Z) dimensions.")
        
        flat_coords = [float(coord) for point in points_list for coord in point]
        handle = _lib.BrlNewArb8AsArb8(*flat_coords)
        return cls(handle)
