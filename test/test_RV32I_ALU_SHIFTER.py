import pytest
from cocotb.binary import BinaryValue

import lib
from test_RV32I_package import RV32I
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_MUX_32X1 import GENERIC_MUX_32X1


class RV32I_ALU_SHIFTER(lib.Entity):
    _package = RV32I

    source = lib.Entity.Input_pin
    shamt = lib.Entity.Input_pin
    select_function = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    MUX_MSB_VECTOR = GENERIC_MUX_2X1
    MUX_source_auxiliar = GENERIC_MUX_2X1
    MUX_DESTINATION = GENERIC_MUX_2X1
    MUX_DATA = GENERIC_MUX_32X1


@RV32I_ALU_SHIFTER.testcase
async def tb_RV32I_ALU_SHIFTER_case_1(dut: RV32I_ALU_SHIFTER, trace: lib.Waveform):
    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00000")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00000")
    dut.select_function.value = BinaryValue("0101")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00001")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111110")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00001")
    dut.select_function.value = BinaryValue("0101")

    await trace.cycle()
    yield trace.check(dut.destination, "01111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("11110")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "11000000000000000000000000000000")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("11101")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "11100000000000000000000000000000")

    dut.source.value = BinaryValue("00000000000000000000000000001000")
    dut.shamt.value = BinaryValue("00010")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000100000")


    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.shamt.value = BinaryValue("11110")
    dut.select_function.value = BinaryValue("0101")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000011")

    dut.source.value = BinaryValue("10000000000000000000000000000000")
    dut.shamt.value = BinaryValue("00001")
    dut.select_function.value = BinaryValue("1101")

    await trace.cycle()
    yield trace.check(dut.destination, "11000000000000000000000000000000")

    dut.source.value = BinaryValue("11000000000000000000000000000000")
    dut.shamt.value = BinaryValue("00010")
    dut.select_function.value = BinaryValue("1101")

    await trace.cycle()
    yield trace.check(dut.destination, "11110000000000000000000000000000")

    dut.source.value = BinaryValue("01111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00001")
    dut.select_function.value = BinaryValue("1101")

    await trace.cycle()
    yield trace.check(dut.destination, "00111111111111111111111111111111")

    dut.source.value = BinaryValue("00111111111111111111111111111111")
    dut.shamt.value = BinaryValue("00010")
    dut.select_function.value = BinaryValue("1101")

    await trace.cycle()
    yield trace.check(dut.destination, "00001111111111111111111111111111")

@pytest.mark.synthesis
def test_RV32I_ALU_SHIFTER_synthesis():
    RV32I_ALU_SHIFTER.build_vhd()
    RV32I_ALU_SHIFTER.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_SHIFTER_testcases():
    RV32I_ALU_SHIFTER.test_with(
        [
            tb_RV32I_ALU_SHIFTER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
