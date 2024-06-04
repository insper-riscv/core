import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_ROM(lib.Entity):
    _package = GENERICS

    address = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_ROM.testcase
async def tb_GENERIC_ROM_case_1(dut: GENERIC_ROM, trace: lib.Waveform):
    dut.address.value = BinaryValue("00000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000001", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000010", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000010")

    await trace.cycle()
    yield trace.check(dut.destination, "00000100", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000011")

    await trace.cycle()
    yield trace.check(dut.destination, "00001000", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000100")

    await trace.cycle()
    yield trace.check(dut.destination, "00010000", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000101")

    await trace.cycle()
    yield trace.check(dut.destination, "00100000", f"For address {dut.address.value}")

    dut.address.value = BinaryValue("00000110")

    await trace.cycle()
    yield trace.check(dut.destination, "01000000", f"For address {dut.address.value}")


@pytest.mark.synthesis
def test_GENERIC_ROM_synthesis():
    GENERIC_ROM.build_vhd()
    GENERIC_ROM.build_netlistsvg()

@pytest.mark.testcases
def test_GENERIC_ROM_testcases():
    GENERIC_ROM.test_with(tb_GENERIC_ROM_case_1)


if __name__ == "__main__":
    lib.run_test(__file__)
