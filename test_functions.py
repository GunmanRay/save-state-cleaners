import pytest 
import obtain_functions as ob
import os
from save_files import Emulators
from validation_functions import RECOGNIZED_SS_EXTENSIONS

@pytest.fixture
def temp_save_dir(tmp_path):
    """A setup for a fake directory, alongside a fake text file that should be
    ignored by the functions being tested"""
    temp_dir = tmp_path / "fake_dir"
    temp_dir.mkdir()

    # A temporary text file that should be ignored by the retrieval functions
    temp_file = temp_dir / "fake_file.txt"
    temp_file.touch()

    yield temp_dir



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
    def test_no_states(self, temp_save_dir):
        assert len(os.listdir(temp_save_dir)) == 1

        assert ob.get_save_states(temp_save_dir) == []

    def test_states(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir / file_ext
            temp_save_state.touch()

        assert len(os.listdir(temp_save_dir)) == 5

        collected_states = ob.get_save_states(temp_save_dir)
        assert len(collected_states) == 4

    def test_different_states(self, temp_save_dir): 
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir / file_ext
            temp_save_state.touch()

            file_ext = f"state.ds{i+1}"
            temp_save_state = temp_save_dir / file_ext
            temp_save_state.touch()

        assert len(os.listdir(temp_save_dir)) == 9
        collected_states = ob.get_save_states(temp_save_dir)
        assert len(collected_states) == 8

    def test_console_specific_save_states(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir / file_ext
            temp_save_state.touch()

            file_ext = f"state.ds{i+1}"
            temp_save_state = temp_save_dir / file_ext
            temp_save_state.touch()

        ds_states = ob.get_specific_save_states(emulator=Emulators.DESMUME, cwd=temp_save_dir)
        gba_states = ob.get_specific_save_states(emulator=Emulators.MGBA, cwd=temp_save_dir)

        assert os.path.splitext(ds_states[1])[1] == ".ds2"
        assert os.path.splitext(gba_states[1])[1] == ".ss2"



if __name__ == '__main__':
    pytest.main()