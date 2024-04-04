import os

import pytest

import utils


class RV32I_FORWARDING_UNIT_ALU(utils.DUT):
    register_source_1        = utils.DUT.Input_pin
    register_source_2        = utils.DUT.Input_pin
    register_destination_mem = utils.DUT.Input_pin
    enable_write_mem         = utils.DUT.Input_pin
    register_destination_wb  = utils.DUT.Input_pin
    enable_write_wb          = utils.DUT.Input_pin
    mux_control_1            = utils.DUT.Output_pin
    mux_control_2            = utils.DUT.Output_pin


def test_RV32I_FORWARDING_UNIT_ALU_synthesis():
    RV32I_FORWARDING_UNIT_ALU.build_vhd()
    # RV32I_FORWARDING_UNIT_ALU.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
