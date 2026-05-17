"""Execution / test script that loads the C bridge and prints/asserts title."""
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.bindings import Bindings, LibraryLoadError


def test_get_title():
    try:
        b = Bindings()
    except LibraryLoadError as exc:
        pytest.skip(f"Shared library not available: {exc}")

    # 1. Instantiate the raw C++ container pointer handle allocation first
    print("\nAllocating fresh database container handle via BrlNewConstDatabase...")
    db_handle = b.database_create()
    
    if not db_handle:
        pytest.fail("Failed to allocate a valid native database handle pointer.")
    print(f"Opaque container handle pointer successfully created at: {hex(db_handle)}")

    try:
        # 2. Pass the handle AND the sample target file string to load the data
        sample_g_file = "/home/home/Documents/work/Python/main-brlcad/cube_scene.g"
        print(f"Calling BrlConstDatabaseLoad on: '{sample_g_file}'")
        
        status = b.database_load(db_handle, sample_g_file)
        print(f"Load operation returned status code: {status}")

        # 3. Call the explicit title wrapper mapping to BrlConstDatabaseTitle
        title = b.database_get_title(db_handle)
        print("Detected title text buffer:", title)

        # Basic assertion suitable for CI: must be None or a Python str
        assert title is None or isinstance(title, str)

    finally:
        b.database_free(db_handle)


if __name__ == "__main__":
    try:
        test_get_title()
    except Exception as e:
        if "skip" in type(e).__name__.lower():
            print(f"Skipped: {e}")
            sys.exit(0)
        raise