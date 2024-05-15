import pytest
from cocotb.binary import BinaryValue

import lib
from test_RV32I_package import RV32I
from test_GENERIC_SIGNAL_EXTENDER import GENERIC_SIGNAL_EXTENDER


class RV32I_TYPE_CONVERTER(lib.Entity):
    _package = RV32I

    select_type = lib.Entity.Input_pin
    source      = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    EXTEND_BYTE = GENERIC_SIGNAL_EXTENDER
    EXTEND_HALFWORD = GENERIC_SIGNAL_EXTENDER



@RV32I_TYPE_CONVERTER.testcase
async def tb_RV32I_TYPE_CONVERTER_case_1(dut: RV32I_TYPE_CONVERTER, trace: lib.Waveform):
    dut.source.value = BinaryValue("10000000100000001000000010000000")
    dut.select_type.value = BinaryValue("000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111110000000")

    dut.select_type.value = BinaryValue("001")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111000000010000000")

    dut.select_type.value = BinaryValue("010")

    await trace.cycle()
    yield trace.check(dut.destination, "10000000100000001000000010000000")

    dut.select_type.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000010000000")

    dut.select_type.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000001000000010000000")

@pytest.mark.synthesis
def test_RV32I_TYPE_CONVERTER_synthesis():
    RV32I_TYPE_CONVERTER.build_vhd()
    RV32I_TYPE_CONVERTER.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_TYPE_CONVERTER_testcases():
    RV32I_TYPE_CONVERTER.test_with(
        [
            tb_RV32I_TYPE_CONVERTER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
