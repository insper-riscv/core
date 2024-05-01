import os

import pytest

import utils
from test_CPU_package import CPU


class CPU_EXECUTION_FOWARDING_UNIT(utils.DUT):
    _package = CPU

    stage_ex_select_source_1     = utils.DUT.Input_pin
    stage_ex_select_source_2     = utils.DUT.Input_pin
    stage_mem_enable_destination = utils.DUT.Input_pin
    stage_mem_select_destination = utils.DUT.Input_pin
    stage_wb_enable_destination  = utils.DUT.Input_pin
    stage_wb_select_destination  = utils.DUT.Input_pin
    stage_id_select_source_1     = utils.DUT.Output_pin
    stage_id_select_source_2     = utils.DUT.Output_pin


@pytest.mark.synthesis
def test_CPU_EXECUTION_FOWARDING_UNIT_synthesis():
    CPU_EXECUTION_FOWARDING_UNIT.build_vhd()
    CPU_EXECUTION_FOWARDING_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
