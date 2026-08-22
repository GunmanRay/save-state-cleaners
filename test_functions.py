import pytest 
import obtain_functions as ob
from save_files import Emulators

class TestSupportedExtensions:
    def test_gba_values_are_same(self):
        assert Emulators.MGBA == Emulators.VBA

    def test_ds_values_are_same(self):
        assert Emulators.DESMUME == Emulators.MELONDS


class TestObtainFunctions:
    def test_no_states(self, tmp_path):
        temp_dir = tmp_path / "fake_dir"
        assert ob.get_save_states(temp_dir) == []
        temp_file = tmp_path / "fake_file.txt"
        assert ob.get_save_states(temp_dir) == []


# class TestValidationMethods(unittest.TestCase):
#     def test_help

if __name__ == '__main__':
    pytest.main()