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

import ctypes 
from ._bindings import _lib
from .Object import Object

class Arb8(Object):
    """8-Vertex Arbitrary Polyhedron primitive tracking container."""
    def __init__(self, *args, **kwargs):
        handle = None
        owned = kwargs.get('owned', True)

        # 1. Handle Input: Arb8(raw_handle)
        if len(args) == 1 and isinstance(args[0], (int, ctypes.c_void_p)):
            handle = args[0]

        # 2. Explicit 8-Point Layout Overload: Arb8(points_list)
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            points_list = args[0]
            if len(points_list) != 8 or any(len(p) != 3 for p in points_list):
                raise ValueError("An explicit Arb8 constructor requires exactly 8 elements of (X, Y, Z) coordinates.")
            flat_coords = [float(coord) for point in points_list for coord in point]
            handle = _lib.BrlNewArb8AsArb8(*flat_coords)

        # 3. Two-Point Forms: RPP bounding box vs Arb4 variant
        elif len(args) == 2:
            p1, p2 = args[0], args[1]
            as_rpp = kwargs.get('is_rpp', True)
            
            # e.g., Arb8(min_pt, max_pt) -> Defaults to RPP
            if as_rpp:
                handle = _lib.BrlNewArb8AsRectengularParallelPiped(
                    float(p1[0]), float(p1[1]), float(p1[2]),
                    float(p2[0]), float(p2[1]), float(p2[2])
                )
            # e.g., Arb8(p1, p2, is_rpp=False) -> Direct Arb4 form
            else:
                handle = _lib.BrlNewArb8AsArb4(
                    float(p1[0]), float(p1[1]), float(p1[2]),
                    float(p2[0]), float(p2[1]), float(p2[2])
                )

        # 4. Fallback Default: Empty parallelpiped bounding box footprint
        if handle is None:
            try:
                handle = _lib.BrlNewArb8()
            except AttributeError:
                handle = _lib.BrlNewArb8AsRectengularParallelPiped(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

        super().__init__(handle=handle, owned=owned)
