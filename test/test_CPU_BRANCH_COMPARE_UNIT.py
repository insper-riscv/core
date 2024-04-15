import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_CPU_BRANCH_COMPARE_UNIT_BIT import CPU_BRANCH_COMPARE_UNIT_BIT

class CPU_BRANCH_COMPARE_UNIT(utils.DUT):
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    branch   = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    cpu_branch_compare_unit_bit = CPU_BRANCH_COMPARE_UNIT_BIT


@CPU_BRANCH_COMPARE_UNIT.testcase
async def tb_CPU_BRANCH_COMPARE_UNIT_case_1(dut: CPU_BRANCH_COMPARE_UNIT, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.selector.value = BinaryValue("000")
    dut.branch.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "1")

    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.selector.value = BinaryValue("001")
    dut.branch.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "1")

    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.selector.value = BinaryValue("100")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000001")
    dut.selector.value = BinaryValue("100")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "0")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.selector.value = BinaryValue("101")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "0")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000001")
    dut.selector.value = BinaryValue("101")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")
    dut.selector.value = BinaryValue("110")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("10000000000000000000000000000000")
    dut.selector.value = BinaryValue("110")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")
    
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.selector.value = BinaryValue("111")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")
    
    dut.source_1.value = BinaryValue("10000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")
    dut.selector.value = BinaryValue("111")
    dut.branch.value = BinaryValue("1")
    
    await trace.cycle()
    yield trace.check(dut.destination, "1")


@pytest.mark.synthesis
def test_CPU_BRANCH_COMPARE_UNIT_synthesis():
    CPU_BRANCH_COMPARE_UNIT.build_vhd()
    # CPU_BRANCH_COMPARE_UNIT.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_BRANCH_COMPARE_UNIT_testcases():
    CPU_BRANCH_COMPARE_UNIT.test_with(
        [
            tb_CPU_BRANCH_COMPARE_UNIT_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
