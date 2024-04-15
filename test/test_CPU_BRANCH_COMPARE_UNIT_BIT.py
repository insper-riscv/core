import os

import pytest
from cocotb.binary import BinaryValue

import utils


class CPU_BRANCH_COMPARE_UNIT_BIT(utils.DUT):
    invert_source_1 = utils.DUT.Input_pin
    invert_source_2 = utils.DUT.Input_pin
    carry_in        = utils.DUT.Input_pin
    slt             = utils.DUT.Input_pin
    source_1        = utils.DUT.Input_pin
    source_2        = utils.DUT.Input_pin
    carry_out       = utils.DUT.Output_pin
    overflow        = utils.DUT.Output_pin

@pytest.mark.synthesis
def test_CPU_BRANCH_COMPARE_UNIT_BIT_synthesis():
    CPU_BRANCH_COMPARE_UNIT_BIT.build_vhd()
    # CPU_BRANCH_COMPARE_UNIT_BIT.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_BRANCH_COMPARE_UNIT_BIT_testcases():
    CPU_BRANCH_COMPARE_UNIT_BIT.test_with(
        [
            #tb_CPU_BRANCH_COMPARE_UNIT_BIT_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
