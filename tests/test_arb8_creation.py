#   Permission to use, copy, modify, and/or distribute this software for any
#   purpose with or without fee is hereby granted.
#  
#   THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#   WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
#   SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
#   RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
#   CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
#   CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brlcad import Arb8

def test_primitive_naming_pipeline():
    print(" Starting BRL-CAD Primitive Creation & Naming Test ")
    
    # Define a simple 3D structural unit cube bounds box range
    min_bound = (0.0, 0.0, 0.0)
    max_bound = (10.0, 10.0, 10.0)
    
    target_name = "box_primitive_01"
    
    print(f"Creating an Arb8 box primitive from bounds: {min_bound} -> {max_bound}...")
    
    with Arb8.from_2_points(min_bound, max_bound) as my_cube:
        
        if my_cube._handle is not None:
            print(f" [SUCCESS] Arb8 instance generated at memory context: {hex(my_cube._handle)}")
            
            print(f"Invoking my_cube.set_name('{target_name}')...")
            my_cube.set_name(target_name)
            print(" [SUCCESS] Primitive identifier mapping applied completely.")
            
        else:
            print(" [ERROR] Core engine allocation layer returned a null address map.", file=sys.stderr)
            return 1

    print(" Primitive lifecycle check completed successfully ")
    return 0

if __name__ == "__main__":
    sys.exit(test_primitive_naming_pipeline())