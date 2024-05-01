import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERICS_package import GENERICS


class GENERIC_ROM(utils.DUT):
    _package = GENERICS

    address = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_ROM.testcase
async def tb_GENERIC_ROM_case_1(dut: GENERIC_ROM, trace: utils.Trace):
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

    dut.address.value = BinaryValue("00000111")

    await trace.cycle()
    yield trace.check(dut.destination, "10000000", f"For address {dut.address.value}")


@pytest.mark.synthesis
def test_GENERIC_ROM_synthesis():
    GENERIC_ROM.build_vhd()
    GENERIC_ROM.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_ROM_testcases():
    GENERIC_ROM.test_with(
        [
            tb_GENERIC_ROM_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
