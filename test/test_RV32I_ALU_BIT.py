import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_RV32I_package import RV32I


class RV32I_ALU_BIT(utils.DUT):
    _package = RV32I

    select_function = utils.DUT.Input_pin
    carry_in = utils.DUT.Input_pin
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin
    carry_out = utils.DUT.Output_pin


@RV32I_ALU_BIT.testcase
async def tb_RV32I_ALU_BIT_case_1(dut: RV32I_ALU_BIT, trace: utils.Trace):
    dut.select_function.value = BinaryValue("000000")
    dut.carry_in.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 0")
    yield trace.check(dut.carry_out, "0", "At cycle 0")

    dut.select_function.value = BinaryValue("000001")
    dut.carry_in.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "1", "At cycle 1")
    yield trace.check(dut.carry_out, "0", "At cycle 1")

    dut.select_function.value = BinaryValue("000011")
    dut.carry_in.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 2")
    yield trace.check(dut.carry_out, "1", "At cycle 2")

    dut.select_function.value = BinaryValue("000110")
    dut.carry_in.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 3")
    yield trace.check(dut.carry_out, "1", "At cycle 3")

    dut.select_function.value = BinaryValue("011000")
    dut.carry_in.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 4")
    yield trace.check(dut.carry_out, "0", "At cycle 4")

    dut.select_function.value = BinaryValue("011001")
    dut.carry_in.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "1", "At cycle 5")
    yield trace.check(dut.carry_out, "0", "At cycle 5")

    dut.select_function.value = BinaryValue("011011")
    dut.carry_in.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 6")
    yield trace.check(dut.carry_out, "1", "At cycle 6")

    dut.select_function.value = BinaryValue("011110")
    dut.carry_in.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "0", "At cycle 7")
    yield trace.check(dut.carry_out, "1", "At cycle 7")


@pytest.mark.synthesis
def test_RV32I_ALU_BIT_synthesis():
    RV32I_ALU_BIT.build_vhd()
    # RV32I_ALU_BIT.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_BIT_testcases():
    RV32I_ALU_BIT.test_with(
        [
            tb_RV32I_ALU_BIT_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
