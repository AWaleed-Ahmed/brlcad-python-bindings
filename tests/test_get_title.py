import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from brlcad import ConstDatabase, FileDatabase, MemoryDatabase

def run_test():
    sample_g_file = "/home/home/Documents/work/Python/main-brlcad/cube_scene.g"
    
    # Initialize the object tracker
    db = ConstDatabase()
    
    # Pure boolean status check flow
    if db.Load(sample_g_file):
        detected_title = db.Title()
        print(f"\n[PASS] Database loaded successfully.")
        print(f"[INFO] Header Title Found: '{detected_title}'")
        
    db_file = FileDatabase()
    if db_file.Load(sample_g_file):
        print(f"[PASS] FileDatabase loaded successfully. Title: '{db_file.Title()}'")

    # EDIT: 3. Add MemoryDatabase check
    db_mem = MemoryDatabase()
    if db_mem.Load(sample_g_file):
        print(f"[PASS] MemoryDatabase loaded successfully. Title: '{db_mem.Title()}'")
        return True

    print("\n[FAIL] Failed to extract correct metadata.")
    return False

if __name__ == "__main__":
    run_test()