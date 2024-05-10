import os
import random

import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_2X1(lib.Entity):
    _package = GENERICS

    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    selector = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


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

@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_stress(dut: GENERIC_MUX_2X1, trace: utils.Trace):
    for _ in range(500_00):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)
        selector = random.getrandbits(1)

        source_1_bits = '{0:0{1}b}'.format(source_1, 32)
        source_2_bits = '{0:0{1}b}'.format(source_2, 32)
        selector_bits = '{0:0{1}b}'.format(selector, 1)
    
        dut.source_1.value = BinaryValue(source_1_bits)
        dut.source_2.value = BinaryValue(source_2_bits)
        dut.selector.value = BinaryValue(selector_bits)
    
        await trace.cycle()

        message = f"source_1: {source_1_bits}, source_2: {source_2_bits}, selector: {selector_bits}"

        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 if selector == 0 else source_2, 32), message)

@GENERIC_MUX_2X1.testcase
async def tb_GENERIC_MUX_2X1_case_stress_5_bits(dut: GENERIC_MUX_2X1, trace: utils.Trace):
    bits = 5
    for i in range(2**bits):
        for j in range(2**bits):
            for k in range(2):
                source_1 = '{0:0{1}b}'.format(i, bits)
                source_2 = '{0:0{1}b}'.format(j, bits)
                selector = '{0:0{1}b}'.format(k, 1)
                
                dut.source_1.value = BinaryValue(source_1)
                dut.source_2.value = BinaryValue(source_2)
                dut.selector.value = BinaryValue(selector)

                message = f"source_1: {source_1}, source_2: {source_2}, selector: {selector}"
                
                await trace.cycle()
                yield trace.check(dut.destination, '{0:0{1}b}'.format(i if k == 0 else j, bits), message)

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
        parameters={"DATA_WIDTH": 32},
    )

@pytest.mark.stress
def test_GENERIC_MUX_2X1_stress_5_bits():
    GENERIC_MUX_2X1.test_with(
        [
            tb_GENERIC_MUX_2X1_case_stress_5_bits,
        ],
        parameters={"DATA_WIDTH": 5},
    )



if __name__ == "__main__":
    lib.run_test(__file__)
