import os
import sys

# Ensure the root directory is on Python's path before importing packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brlcad import FileDatabase


def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    argc = len(argv)
    ret = 1

    if argc < 2 or argv[1] is None:
        print(f"Usage: {argv[0]} <test type>", file=sys.stderr)
    else:
        if argv[1] == "getTitle":
            
            with FileDatabase() as database:
                filename = "gettitle.g"

                if not os.path.exists(filename):
                    print(f"Error: {filename} not found", file=sys.stderr)
                    return 1

                if database.Load(filename):
                    database.SetTitle("get Title")
                    
                    print(f"[SUCCESS] Updated Title value: '{database.Title()}'")
                    ret = 0
                else:
                    print("Could not load file", file=sys.stderr)
        else:
            print(f"Unknown test type: {argv[1]}", file=sys.stderr)

    return ret


if __name__ == "__main__":
    sys.exit(main())