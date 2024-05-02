import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_4X1(lib.Entity):
    _package = GENERICS

    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    source_3 = lib.Entity.Input_pin
    source_4 = lib.Entity.Input_pin
    selector = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_1(dut: GENERIC_MUX_4X1, trace: lib.Waveform):
    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000010")
    dut.source_3.value = BinaryValue("00000011")
    dut.source_4.value = BinaryValue("00000100")
    dut.selector.value = BinaryValue("00")

    await trace.cycle()
    yield trace.check(dut.destination, "00000001")

    dut.selector.value = BinaryValue("01")

    await trace.cycle()
    yield trace.check(dut.destination, "00000010")

    dut.selector.value = BinaryValue("10")

    await trace.cycle()
    yield trace.check(dut.destination, "00000011")

    dut.selector.value = BinaryValue("11")

    await trace.cycle()
    yield trace.check(dut.destination, "00000100")


@pytest.mark.synthesis
def test_GENERIC_MUX_4X1_synthesis():
    GENERIC_MUX_4X1.build_vhd()
    GENERIC_MUX_4X1.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_MUX_4X1_testcases():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
