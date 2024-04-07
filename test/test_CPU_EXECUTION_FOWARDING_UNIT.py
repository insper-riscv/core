import os

import pytest

import utils


class CPU_EXECUTION_FOWARDING_UNIT(utils.DUT):
    register_source_1        = utils.DUT.Input_pin
    register_source_2        = utils.DUT.Input_pin
    register_destination_mem = utils.DUT.Input_pin
    enable_write_mem         = utils.DUT.Input_pin
    register_destination_wb  = utils.DUT.Input_pin
    enable_write_wb          = utils.DUT.Input_pin
    mux_control_1            = utils.DUT.Output_pin
    mux_control_2            = utils.DUT.Output_pin


def test_CPU_EXECUTION_FOWARDING_UNIT_synthesis():
    CPU_EXECUTION_FOWARDING_UNIT.build_vhd()
    # CPU_EXECUTION_FOWARDING_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
