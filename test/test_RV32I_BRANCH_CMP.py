import os

import pytest
from cocotb.binary import BinaryValue

import utils

class RV32I_BRANCH_CMP(utils.DUT):
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    branch   = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@RV32I_BRANCH_CMP.testcase
async def tb_RV32I_BRANCH_CMP_case_1(dut: RV32I_BRANCH_CMP, trace: utils.Trace):
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
def test_RV32I_BRANCH_CMP_synthesis():
    RV32I_BRANCH_CMP.build_vhd()
    # RV32I_BRANCH_CMP.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_BRANCH_CMP_testcases():
    RV32I_BRANCH_CMP.test_with(
        [
            tb_RV32I_BRANCH_CMP_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
