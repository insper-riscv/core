import pytest
from cocotb.binary import BinaryValue

import lib
from test_RV32I_package import RV32I
from test_RV32I_ALU_BIT import RV32I_ALU_BIT
from test_RV32I_ALU_SHIFTER import RV32I_ALU_SHIFTER


class RV32I_ALU(lib.Device):
    _package = RV32I

    select_function = lib.Device.Input_pin
    source_1 = lib.Device.Input_pin
    source_2 = lib.Device.Input_pin
    destination = lib.Device.Output_pin

    bit_to_bit = RV32I_ALU_BIT
    generic_shifter = RV32I_ALU_SHIFTER


@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_1(dut: RV32I_ALU, trace: lib.Waveform):
    dut.select_function.value = BinaryValue("0111")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 0")

    dut.select_function.value = BinaryValue("0110") # 000001
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 1")

    dut.select_function.value = BinaryValue("0000") # 000011
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("00000000000000001111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 2")

    dut.select_function.value = BinaryValue("1011") # 110111
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 3")

    dut.select_function.value = BinaryValue("1000") # 001000
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001", "At 4")

    dut.select_function.value = BinaryValue("1110") # 010001
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 5")

    dut.select_function.value = BinaryValue("1000") # 001011
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("11111111111111110000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 6")

    dut.select_function.value = BinaryValue("1010") # 010111
    dut.source_1.value = BinaryValue("00000000000000000000000000000010")
    dut.source_2.value = BinaryValue("00000000000000000000000000000100")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001", "At 7")

    dut.select_function.value = BinaryValue("0001") # 000100
    dut.source_1.value = BinaryValue("00000000000000000000000000001000")
    dut.source_2.value = BinaryValue("00000000000000000000000000001000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000100000000000", "At 8")


@pytest.mark.synthesis
def test_RV32I_ALU_synthesis():
    RV32I_ALU.build_vhd()
    # RV32I_ALU.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_testcases():
    RV32I_ALU.test_with(
        [
            tb_RV32I_ALU_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
