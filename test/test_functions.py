import pytest 
from savestatecleaners import obtain_functions as ob
from savestatecleaners import deletion_functions as delete
import os
from savestatecleaners.save_files import Emulators
from savestatecleaners.obtain_functions import RECOGNIZED_SS_EXTENSIONS

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
        
class TestDeletionFunctions: 
    def test_deletion_general(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        assert len(os.listdir(temp_save_dir["root"])) == 7
        assert len(ob.get_save_states(temp_save_dir["root"])) == 4

        delete.delete_from_cwd(temp_save_dir["root"])
        assert len(os.listdir(temp_save_dir["root"])) == 3
        assert len(ob.get_save_states(temp_save_dir["root"])) == 0

    def test_deletion_level_1(self, temp_save_dir):
        for i in range (0, 4):
            file_ext = f"state.ss{i+1}"
            temp_save_state = temp_save_dir["root"] / file_ext
            temp_save_state.touch()

        l2_save_state = temp_save_dir["l2_1"] / "state.ss8"
        l2_save_state.touch()

        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 5
        delete.delete_from_cwd(temp_save_dir["root"], delete_from_subdirs=False)
        assert  len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 1

    def test_deletion_level_2(self, temp_save_dir):
        for i in range(0, 6): 
            state2_1 = temp_save_dir["l2_1"] / f"state.ss{i}"
            state2_1.touch()

            state2_2 = temp_save_dir["l2_2"] / f"state.ss{i}"
            state2_2.touch()

        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 12
        delete.delete_from_cwd(temp_save_dir["root"], delete_from_subdirs=True)
        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 0

    def test_deletion_all_levels(self, temp_save_dir):
        for i in range(0, 2):
            state1 = temp_save_dir["root"] / f"state.ds{i}"
            state1.touch()

        for i in range(0, 6): 
            state2_1 = temp_save_dir["l2_1"] / f"state.ss{i}"
            state2_1.touch()

            state2_2 = temp_save_dir["l2_2"] / f"state.ss{i}"
            state2_2.touch()

        state3 = temp_save_dir["l3"] / "state.ds8"
        state3.touch()

        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 15
        delete.delete_from_cwd(temp_save_dir["root"], delete_from_subdirs=True)
        assert len(ob.get_save_states(temp_save_dir["root"], scan_subdirs=True)) == 0



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