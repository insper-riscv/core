import pytest
from cocotb.binary import BinaryValue

import lib
from test_RV32I_package import RV32I
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1
from test_GENERIC_CARRY_LOOKAHEAD import GENERIC_CARRY_LOOKAHEAD
from test_RV32I_ALU_SHIFTER import RV32I_ALU_SHIFTER


class RV32I_ALU(lib.Entity):
    _package = RV32I

    select_function = lib.Entity.Input_pin
    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    overflow = lib.Entity.Output_pin
    destination = lib.Entity.Output_pin

    MUX_SOURCE_2 = GENERIC_MUX_2X1
    CARRY_LOOKAHEAD = GENERIC_CARRY_LOOKAHEAD
    SHIFTER = RV32I_ALU_SHIFTER
    MUX_DESTINATION_1 = GENERIC_MUX_4X1
    MUX_DESTINATION_2 = GENERIC_MUX_4X1
    MUX_DESTINATION_3 = GENERIC_MUX_2X1


@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_1(dut: RV32I_ALU, trace: lib.Waveform):
    dut.select_function.value = BinaryValue("0111")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    trace.set_scale(2)
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
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
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
    RV32I_ALU.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_testcases():
    RV32I_ALU.test_with(
        [
            tb_RV32I_ALU_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
