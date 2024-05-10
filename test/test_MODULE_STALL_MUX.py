import os

import pytest
from cocotb.binary import BinaryValue

import lib
from test_CPU_package import CPU


class MODULE_STALL_MUX(lib.Entity):
    _package = CPU

    control_ex_in = lib.Entity.Input_pin
    control_mem_in = lib.Entity.Input_pin
    control_wb_in = lib.Entity.Input_pin
    selector = lib.Entity.Input_pin
    control_ex_out = lib.Entity.Output_pin
    control_mem_out = lib.Entity.Output_pin
    control_wb_out = lib.Entity.Output_pin
    

@pytest.mark.synthesis
def test_MODULE_STALL_MUX_synthesis():
    MODULE_STALL_MUX.build_vhd()
    MODULE_STALL_MUX.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
