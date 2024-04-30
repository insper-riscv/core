import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_MODULES_package import MODULES
from test_RV32I_BRANCH_CONTROLLER import RV32I_BRANCH_CONTROLLER
from test_GENERIC_COMPARATOR import GENERIC_COMPARATOR

class MODULE_BRANCH_COMPARE_UNIT(utils.DUT):
    _package = MODULES

    enable = utils.DUT.Input_pin
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    select_function = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    compare = RV32I_BRANCH_CONTROLLER
    comparator = GENERIC_COMPARATOR


@MODULE_BRANCH_COMPARE_UNIT.testcase
async def tb_MODULE_BRANCH_COMPARE_UNIT_case_1(dut: MODULE_BRANCH_COMPARE_UNIT, trace: utils.Trace):
    dut.enable.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.select_function.value = BinaryValue("0000")

    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 1")

    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 2")

    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0100")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 3")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0100")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 4")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0101")
    
    await trace.cycle()
    yield trace.check(dut.destination, "0", "At 5")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0101")
    
    await trace.cycle()
    yield trace.check(dut.destination, "0", "At 6")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.select_function.value = BinaryValue("0110")

    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 7")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000000")
    dut.select_function.value = BinaryValue("0110")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 8")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.select_function.value = BinaryValue("0111")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 9")
    
    dut.source_1.value = BinaryValue("10000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.select_function.value = BinaryValue("0111")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1", "At 10")


@pytest.mark.synthesis
def test_MODULE_BRANCH_COMPARE_UNIT_synthesis():
    MODULE_BRANCH_COMPARE_UNIT.build_vhd()
    # MODULE_BRANCH_COMPARE_UNIT.build_netlistsvg()


@pytest.mark.testcases
def test_MODULE_BRANCH_COMPARE_UNIT_testcases():
    MODULE_BRANCH_COMPARE_UNIT.test_with(
        [
            tb_MODULE_BRANCH_COMPARE_UNIT_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
