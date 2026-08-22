import pytest 
import obtain_functions as ob
import os
from save_files import Emulators
from validation_functions import RECOGNIZED_SS_EXTENSIONS

class TestSupportedExtensions:
    def test_gba_values_are_same(self):
        assert Emulators.MGBA == Emulators.VBA

    def test_ds_values_are_same(self):
        assert Emulators.DESMUME == Emulators.MELONDS

    def test_placements(self):
        assert RECOGNIZED_SS_EXTENSIONS[Emulators.MGBA.value] == "*.ss[0-9]"
        assert RECOGNIZED_SS_EXTENSIONS[Emulators.VBA.value] == "*.ss[0-9]"
        assert RECOGNIZED_SS_EXTENSIONS[Emulators.DESMUME.value] == "*.ds[0-9]"
        assert RECOGNIZED_SS_EXTENSIONS[Emulators.MELONDS.value] == "*.ds[0-9]"


class TestObtainFunctions:
    def test_no_states(self, tmp_path):
        temp_dir = tmp_path / "fake_dir"
        temp_dir.mkdir()

        assert ob.get_save_states(temp_dir) == []

        temp_file = temp_dir / "fake_file.txt"
        temp_file.write_text("Dummy data")
        assert len(os.listdir(temp_dir)) == 1

        assert ob.get_save_states(temp_dir) == []

    def test_states(self, tmp_path):
        temp_dir = tmp_path / "fake_dir"
        temp_dir.mkdir()

        temp_file = temp_dir / "fake_file.txt"
        temp_file.write_text("Dummy data")
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_dir / file_ext
            temp_save_state.write_text("Dummy data")

        assert len(os.listdir(temp_dir)) == 5

        collected_states = ob.get_save_states(temp_dir)
        assert len(collected_states) == 4

    def test_different_states(self, tmp_path): 
        temp_dir = tmp_path / "fake_dir"
        temp_dir.mkdir()

        temp_file = temp_dir / "fake_file.txt"
        temp_file.write_text("Dummy data")
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_dir / file_ext
            temp_save_state.write_text("Dummy data")

            file_ext = f"state.ds{i+1}"
            temp_save_state = temp_dir / file_ext
            temp_save_state.write_text("Dummy data")

        assert len(os.listdir(temp_dir)) == 9
        collected_states = ob.get_save_states(temp_dir)
        assert len(collected_states) == 8
            


if __name__ == '__main__':
    pytest.main()