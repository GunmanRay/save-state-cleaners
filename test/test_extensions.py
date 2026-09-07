import pytest 
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

