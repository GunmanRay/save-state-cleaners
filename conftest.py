import sys
from pathlib import Path
import pytest

# Automatically add the project root to sys.path for pytest
sys.path.insert(0, str(Path(__file__).parent))

LEVEL2_1 = "fake_dir_level2_1"
LEVEL2_2 = "fake_dir_level2_2"
LEVEL3 = "fake_dir_level3"

LEVEL2_1 = "fake_dir_level2_1"
LEVEL2_2 = "fake_dir_level2_2"
LEVEL3 = "fake_dir_level3"

@pytest.fixture
def temp_save_dir(tmp_path):
    """A setup for a fake directory, alongside a fake text file that should be
    ignored by the functions being tested"""
    temp_dir = tmp_path / "fake_dir"
    temp_dir.mkdir()

    temp_dir_level_2_1 = temp_dir / LEVEL2_1
    temp_dir_level_2_1.mkdir()

    temp_dir_level_2_2 = temp_dir / LEVEL2_2
    temp_dir_level_2_2.mkdir()

    temp_dir_level_3 = temp_dir_level_2_1 / LEVEL3
    temp_dir_level_3.mkdir()

    # A temporary text file that should be ignored by the retrieval functions
    temp_file = temp_dir / "fake_file.txt"
    temp_file.touch()

    return {
        "root": temp_dir,
        "l2_1": temp_dir_level_2_1,
        "l2_2": temp_dir_level_2_2,
        "l3": temp_dir_level_3
    }