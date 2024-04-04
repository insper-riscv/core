import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class GENERIC_MUX_4X1(utils.DUT):
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    source_3 = utils.DUT.Input_pin
    source_4 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux_1 = GENERIC_MUX_2X1
    mux_2 = GENERIC_MUX_2X1


@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_1(dut: GENERIC_MUX_4X1, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000010")
    dut.source_3.value = BinaryValue("00000000000000000000000000000011")
    dut.source_4.value = BinaryValue("00000000000000000000000000000100")
    dut.selector.value = BinaryValue("00")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001")

    dut.selector.value = BinaryValue("01")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000010")

    dut.selector.value = BinaryValue("10")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000011")

    dut.selector.value = BinaryValue("11")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000100")


def test_GENERIC_MUX_4X1_synthesis():
    GENERIC_MUX_4X1.build_vhd()
    # GENERIC_MUX_4X1.build_netlistsvg()


def test_GENERIC_MUX_4X1_testcases():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
