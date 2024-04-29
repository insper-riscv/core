import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_2X1(lib.Device):
    _package = GENERICS

    source_1 = lib.Device.Input_pin
    source_2 = lib.Device.Input_pin
    selector = lib.Device.Input_pin
    destination = lib.Device.Output_pin


@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_1(dut: GENERIC_MUX_2X1, trace: lib.Waveform):
    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000010")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00000001")

    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000010")
    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "00000010")

    dut.source_1.value = BinaryValue("00000011")
    dut.source_2.value = BinaryValue("00000100")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00000011")

    dut.source_1.value = BinaryValue("00000011")
    dut.source_2.value = BinaryValue("00000100")
    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "00000100")


@pytest.mark.synthesis
def test_GENERIC_MUX_2X1_synthesis():
    GENERIC_MUX_2X1.build_vhd()
    # GENERIC_MUX_2X1.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_MUX_2X1_testcases():
    GENERIC_MUX_2X1.test_with(
        [
            tb_GENERIC_MUX_2X1_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
