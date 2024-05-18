import os

import pytest
from cocotb.binary import BinaryValue

import lib
from test_CPU_package import CPU


class CPU_HAZZARD_CONTROL_UNIT(lib.Entity):
    _package = CPU

    stage_id_select_source_1     = lib.Entity.Input_pin
    stage_id_select_source_2     = lib.Entity.Input_pin
    stage_ex_enable_read         = lib.Entity.Input_pin
    stage_ex_enable_destination  = lib.Entity.Input_pin
    stage_ex_select_destination  = lib.Entity.Input_pin
    stage_mem_enable_read        = lib.Entity.Input_pin
    stage_mem_select_destination = lib.Entity.Input_pin
    stall_branch                 = lib.Entity.Output_pin
    destination                  = lib.Entity.Output_pin

@pytest.mark.synthesis
def test_CPU_HAZZARD_CONTROL_UNIT_synthesis():
    CPU_HAZZARD_CONTROL_UNIT.build_vhd()
    CPU_HAZZARD_CONTROL_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
