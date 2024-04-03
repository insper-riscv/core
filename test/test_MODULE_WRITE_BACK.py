import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_WRITE_BACK(utils.DUT):
    source_memory = utils.DUT.Input_pin
    source_ex = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux = GENERIC_MUX_2X1


@MODULE_WRITE_BACK.testcase
async def tb_MODULE_WRITE_BACK_case_1(dut: MODULE_WRITE_BACK, trace: utils.Trace):
    dut.source_memory.value = BinaryValue("00001111000011110000111100001111")
    dut.source_ex.value = BinaryValue("11110000111100001111000011110000")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00001111000011110000111100001111")

    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "11110000111100001111000011110000")

    dut.source_memory.value = BinaryValue("00000000000000000000000000000000")
    dut.source_ex.value = BinaryValue("11111111111111111111111111111111")
    dut.selector.value = BinaryValue("0")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000")

    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")


def test_MODULE_WRITE_BACK_synthesis():
    MODULE_WRITE_BACK.build_vhd()
    # MODULE_WRITE_BACK.build_netlistsvg()


def test_MODULE_WRITE_BACK_testcases():
    MODULE_WRITE_BACK.test_with(
        [
            tb_MODULE_WRITE_BACK_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
