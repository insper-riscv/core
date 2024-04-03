import os

import pytest
from cocotb.binary import BinaryValue

import utils


class GENERIC_MUX_2X1(utils.DUT):
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_1(dut: GENERIC_MUX_2X1, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000010")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001")

    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000010")
    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000010")

    dut.source_1.value = BinaryValue("00000000000000000000000000000011")
    dut.source_2.value = BinaryValue("00000000000000000000000000000100")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000011")

    dut.source_1.value = BinaryValue("00000000000000000000000000000011")
    dut.source_2.value = BinaryValue("00000000000000000000000000000100")
    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000100")


def test_GENERIC_MUX_2X1_synthesis():
    GENERIC_MUX_2X1.build_vhd()
    # GENERIC_MUX_2X1.build_netlistsvg()


def test_GENERIC_MUX_2X1_testcases():
    GENERIC_MUX_2X1.test_with(
        [
            tb_GENERIC_MUX_2X1_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
