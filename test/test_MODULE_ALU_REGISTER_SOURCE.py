import os

import pytest

import utils
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1


class MODULE_ALU_REGISTER_SOURCE(utils.DUT):
    register_source_1     = utils.DUT.Input_pin
    register_source_2     = utils.DUT.Input_pin
    forwarding_mem_source = utils.DUT.Input_pin
    forwarding_wb_source  = utils.DUT.Input_pin
    select_source_1       = utils.DUT.Input_pin
    select_source_2       = utils.DUT.Input_pin
    data_source_1         = utils.DUT.Output_pin
    data_source_2         = utils.DUT.Output_pin

    mux_register_alu_1 = GENERIC_MUX_4X1
    mux_register_alu_2 = GENERIC_MUX_4X1


def test_MODULE_ALU_REGISTER_SOURCE_synthesis():
    MODULE_ALU_REGISTER_SOURCE.build_vhd()
    # MODULE_ALU_REGISTER_SOURCE.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
