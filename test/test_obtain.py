import pytest 
from savestatecleaners import obtain_functions as ob
import os
from savestatecleaners.save_files import Emulators
from savestatecleaners.obtain_functions import RECOGNIZED_SS_EXTENSIONS

class TestObtainFunctions:
    def test_no_states(self, temp_save_dir):
        assert len(os.listdir(temp_save_dir["root"])) == 3
        assert len(os.listdir(temp_save_dir["root"])) == 3

        assert ob.get_save_states(temp_save_dir["root"]) == []

    def test_states(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        assert len(os.listdir(temp_save_dir["root"])) == 7
        assert len(os.listdir(temp_save_dir["root"])) == 7

        collected_states = ob.get_save_states(temp_save_dir["root"])
        assert len(collected_states) == 4

    def test_different_states(self, temp_save_dir): 
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

            file_ext = f"state.ds{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        assert len(os.listdir(temp_save_dir["root"])) == 11
        assert len(os.listdir(temp_save_dir["root"])) == 11
        collected_states = ob.get_save_states(temp_save_dir["root"])
        assert len(collected_states) == 8

    def test_console_specific_save_states(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

            file_ext = f"state.ds{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        ds_states = ob.get_specific_save_states(emulator=Emulators.DESMUME, cwd=temp_save_dir["root"])
        gba_states = ob.get_specific_save_states(emulator=Emulators.MGBA, cwd=temp_save_dir["root"])

        assert os.path.splitext(ds_states[1])[1] == ".ds2"
        assert os.path.splitext(gba_states[1])[1] == ".ss2"

    def test_recursive_search_only_level_1(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        non_save_state = temp_save_dir["l3"] / "temp.txt"
        non_save_state.touch()

        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 4

    def test_recursive_search_only_level_2(self, temp_save_dir):    
            save_state_l2_1 = temp_save_dir["l2_1"] / "state.ss5"
            save_state_l2_1.touch()
            save_state_l2_2 = temp_save_dir["l2_2"] / "state.ss5"
            save_state_l2_2.touch()

            assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 2

    def test_recursive_search_muultiple_levels(self, temp_save_dir):
        for i in range (0, 4):
                file_ext = f"state.ss{i+1}"
                temp_save_state = temp_save_dir["root"] / file_ext
                temp_save_state.touch()

        for i in range (0, 5):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["l3"] / file_ext
            temp_save_state.touch()

        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 9

if __name__ == '__main__':
    pytest.main()