import os

import pytest
from cocotb.binary import BinaryValue

import utils


class GENERIC_SHIFTER(utils.DUT):
    source      = utils.DUT.Input_pin
    selector_1  = utils.DUT.Input_pin
    selector_2  = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin
    destination_q = utils.DUT.Output_pin


@GENERIC_SHIFTER.testcase
async def tb_GENERIC_SHIFTER_case_1(dut: GENERIC_SHIFTER, trace: utils.Trace):
    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("00000")
    dut.selector_2.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("00000")
    dut.selector_2.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("00001")
    dut.selector_2.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111110")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("00001")
    dut.selector_2.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "01111111111111111111111111111111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11110")
    dut.selector_2.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "11000000000000000000000000000000")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11101")
    dut.selector_2.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "11100000000000000000000000000000")

    dut.source.value = BinaryValue("00000000000000000000000000001000")
    dut.selector_1.value = BinaryValue("00010")
    dut.selector_2.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000100000")


    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11110")
    dut.selector_2.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000011")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11101")
    dut.selector_2.value = BinaryValue("101")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000111")

    dut.source.value = BinaryValue("11111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11101")
    dut.selector_2.value = BinaryValue("110")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source.value = BinaryValue("01111111111111111111111111111111")
    dut.selector_1.value = BinaryValue("11100")
    dut.selector_2.value = BinaryValue("110")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000001111")

@pytest.mark.synthesis
def test_GENERIC_SHIFTER_synthesis():
    GENERIC_SHIFTER.build_vhd()
    # GENERIC_SHIFTER.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_SHIFTER_testcases():
    GENERIC_SHIFTER.test_with(
        [
            tb_GENERIC_SHIFTER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])