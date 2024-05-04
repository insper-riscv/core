import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_CPU_package import CPU


class CPU_HAZZARD_CONTROL_UNIT(utils.DUT):
    _package = CPU

    stage_id_select_source_1     = utils.DUT.Input_pin
    stage_id_select_source_2     = utils.DUT.Input_pin
    stage_ex_enable_write        = utils.DUT.Input_pin
    stage_ex_select_destination  = utils.DUT.Input_pin
    stage_mem_enable_read        = utils.DUT.Input_pin
    stage_mem_select_destination = utils.DUT.Input_pin
    stall_branch                 = utils.DUT.Output_pin
    destination                  = utils.DUT.Output_pin

@pytest.mark.synthesis
def test_CPU_HAZZARD_CONTROL_UNIT_synthesis():
    CPU_HAZZARD_CONTROL_UNIT.build_vhd()
    CPU_HAZZARD_CONTROL_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
