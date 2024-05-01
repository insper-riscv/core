import os

import pytest

import utils
from test_MODULES_package import MODULES
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_BRANCH_UNIT(utils.DUT):
    _package = MODULES

    ADDER_1 = GENERIC_ADDER
    ADDER_2 = GENERIC_ADDER
    MUX_1 = GENERIC_MUX_2X1


@pytest.mark.synthesis
def test_MODULE_BRANCH_UNIT_synthesis():
    MODULE_BRANCH_UNIT.build_vhd()
    MODULE_BRANCH_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
