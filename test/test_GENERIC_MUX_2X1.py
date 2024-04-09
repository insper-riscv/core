import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERICS_package import GENERICS


class GENERIC_MUX_2X1(utils.DUT):
    _package = GENERICS

    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_1(dut: GENERIC_MUX_2X1, trace: utils.Trace):
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

@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_stress(dut: GENERIC_MUX_2X1, trace: utils.Trace):
    bits = 5
    for i in range(2**bits):
        for j in range(2**bits):
            for k in range(2):
                dut.source_1.value = BinaryValue(utils.convert_to_binstr(i, bits))
                dut.source_2.value = BinaryValue(utils.convert_to_binstr(j, bits))
                dut.selector.value = BinaryValue(utils.convert_to_binstr(k, 1))

                await trace.cycle()
                yield trace.check(dut.destination, utils.convert_to_binstr(i if k == 0 else j, bits))

@pytest.mark.synthesis
def test_GENERIC_MUX_2X1_synthesis():
    GENERIC_MUX_2X1.build_vhd()
    GENERIC_MUX_2X1.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_MUX_2X1_testcases():
    GENERIC_MUX_2X1.test_with(
        [
            tb_GENERIC_MUX_2X1_case_1,
        ]
    )

@pytest.mark.stress
def test_GENERIC_MUX_2X1_stress():
    GENERIC_MUX_2X1.test_with(
        [
            tb_GENERIC_MUX_2X1_case_stress,
        ],
        parameters={"DATA_WIDTH": 5},
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
