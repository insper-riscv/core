import os

import pytest

import utils
from test_MODULE_PC import MODULE_PC


class STAGE_IF(utils.DUT):
    control = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    address_jump = utils.DUT.Input_pin
    address_program = utils.DUT.Output_pin

    module_pc = MODULE_PC


def test_STAGE_IF_synthesis():
    STAGE_IF.build_vhd()
    # STAGE_IF.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
