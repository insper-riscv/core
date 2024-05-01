import os
import random

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERICS_package import GENERICS


class GENERIC_ADDER(utils.DUT):
    _package = GENERICS

    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_case_1(dut: GENERIC_ADDER, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000000")
    dut.source_2.value = BinaryValue("00000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000")

    dut.source_1.value = BinaryValue("00000000")
    dut.source_2.value = BinaryValue("00000001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000001")

    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000010")

    dut.source_1.value = BinaryValue("10101010")
    dut.source_2.value = BinaryValue("01010101")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111")

    dut.source_1.value = BinaryValue("10101010")
    dut.source_2.value = BinaryValue("10101010")

    await trace.cycle()
    yield trace.check(dut.destination, "01010100")

    dut.source_1.value = BinaryValue("11111110")
    dut.source_2.value = BinaryValue("00000001")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111")


@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_stress(dut: GENERIC_ADDER, trace: utils.Trace):
    for _ in range(1_000_000):
        source_1 = random.getrandbits(8)
        source_2 = random.getrandbits(8)
    
        dut.source_1.value = BinaryValue(utils.convert_to_binstr(source_1, 8))
        dut.source_2.value = BinaryValue(utils.convert_to_binstr(source_2, 8))
    
        await trace.cycle()

        message = f"source_1: {utils.convert_to_binstr(source_1, 8)}, source_2: {utils.convert_to_binstr(source_2, 8)}"

        yield trace.check(dut.destination, utils.convert_to_binstr(source_1 + source_2, 8), message)


@pytest.mark.synthesis
def test_GENERIC_ADDER_synthesis():
    GENERIC_ADDER.build_vhd()
    GENERIC_ADDER.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_ADDER_testcases():
    GENERIC_ADDER.test_with(
        [
            tb_GENERIC_ADDER_case_1,
        ]
    )


@pytest.mark.stress
def test_GENERIC_ADDER_stress():
    GENERIC_ADDER.test_with(
        [
            tb_GENERIC_ADDER_stress
        ]
    )

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
