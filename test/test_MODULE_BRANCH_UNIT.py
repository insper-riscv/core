import pytest

import lib
from test_MODULES_package import MODULES
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_BRANCH_UNIT(lib.Entity):
    _package = MODULES

    selector = lib.Entity.Input_pin
    source_program = lib.Entity.Input_pin
    source_immediate = lib.Entity.Input_pin
    source_register = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    ADDER_1 = GENERIC_ADDER
    ADDER_2 = GENERIC_ADDER
    MUX_1 = GENERIC_MUX_2X1


@pytest.mark.synthesis
def test_MODULE_BRANCH_UNIT_synthesis():
    MODULE_BRANCH_UNIT.build_vhd()
    MODULE_BRANCH_UNIT.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
