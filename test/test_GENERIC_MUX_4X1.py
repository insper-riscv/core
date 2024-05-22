import os
import random

import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_4X1(lib.Entity):
    _package = GENERICS

    selector = lib.Entity.Input_pin
    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    source_3 = lib.Entity.Input_pin
    source_4 = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_1(dut: GENERIC_MUX_4X1, trace: lib.Waveform):
    dut.selector.value = BinaryValue("00")
    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000010")
    dut.source_3.value = BinaryValue("00000011")
    dut.source_4.value = BinaryValue("00000100")

    await trace.cycle()
    yield trace.check(dut.destination, "00000001")

    dut.selector.value = BinaryValue("01")

    await trace.cycle()
    yield trace.check(dut.destination, "00000010")

    dut.selector.value = BinaryValue("10")

    await trace.cycle()
    yield trace.check(dut.destination, "00000011")

    dut.selector.value = BinaryValue("11")

    await trace.cycle()
    yield trace.check(dut.destination, "00000100")

@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_coverage(dut: GENERIC_MUX_4X1, trace: lib.Waveform):
    trace.disable()

    for _ in range(250_000):
        selector = random.getrandbits(2)
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)
        source_3 = random.getrandbits(32)
        source_4 = random.getrandbits(32)

        selector_bits = '{0:0{1}b}'.format(selector, 2)
        source_1_bits = '{0:0{1}b}'.format(source_1, 32)
        source_2_bits = '{0:0{1}b}'.format(source_2, 32)
        source_3_bits = '{0:0{1}b}'.format(source_3, 32)
        source_4_bits = '{0:0{1}b}'.format(source_4, 32)

        dut.selector.value = BinaryValue(selector_bits)
        dut.source_1.value = BinaryValue(source_1_bits)
        dut.source_2.value = BinaryValue(source_2_bits)
        dut.source_3.value = BinaryValue(source_3_bits)
        dut.source_4.value = BinaryValue(source_4_bits)

        await trace.cycle()

        message = f"source_1: {source_1_bits}, source_2: {source_2_bits}, source_3: {source_3_bits}, source_4: {source_4_bits}, selector: {selector_bits}"

        if selector == 0:
            yield trace.check(dut.destination, source_1_bits, message)
        if selector == 1:
            yield trace.check(dut.destination, source_2_bits, message)
        if selector == 2:
            yield trace.check(dut.destination, source_3_bits, message)
        if selector == 3:
            yield trace.check(dut.destination, source_4_bits, message)

@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_coverage_3_bits(dut: GENERIC_MUX_4X1, trace: lib.Waveform):
    trace.disable()

    bits = 3
    for value_1 in range(2**bits):
        for value_2 in range(2**bits):
            for value_3 in range(2**bits):
                for value_4 in range(2**bits):
                    for selector in range(4):
                        selector = '{0:0{1}b}'.format(selector, 2)
                        source_1 = '{0:0{1}b}'.format(value_1, bits)
                        source_2 = '{0:0{1}b}'.format(value_2, bits)
                        source_3 = '{0:0{1}b}'.format(value_3, bits)
                        source_4 = '{0:0{1}b}'.format(value_4, bits)

                        dut.selector.value = BinaryValue(selector)
                        dut.source_1.value = BinaryValue(source_1)
                        dut.source_2.value = BinaryValue(source_2)
                        dut.source_3.value = BinaryValue(source_3)
                        dut.source_4.value = BinaryValue(source_4)

                        message = f"source_1: {source_1}, source_2: {source_2}, selector: {selector}"

                        await trace.cycle()

                        if selector == 0:
                            yield trace.check(dut.destination, '{0:0{1}b}'.format(value_1, bits), message)
                        if selector == 1:
                            yield trace.check(dut.destination, '{0:0{1}b}'.format(value_2, bits), message)
                        if selector == 2:
                            yield trace.check(dut.destination, '{0:0{1}b}'.format(value_3, bits), message)
                        if selector == 3:
                            yield trace.check(dut.destination, '{0:0{1}b}'.format(value_4, bits), message)


@pytest.mark.synthesis
def test_GENERIC_MUX_4X1_synthesis():
    GENERIC_MUX_4X1.build_vhd()
    GENERIC_MUX_4X1.build_netlistsvg()

@pytest.mark.testcases
def test_GENERIC_MUX_4X1_testcases():
    GENERIC_MUX_4X1.test_with(tb_GENERIC_MUX_4X1_case_1)

@pytest.mark.coverage
def test_GENERIC_MUX_4X1_stress():
    GENERIC_MUX_4X1.test_with(tb_GENERIC_MUX_4X1_case_coverage, {
        "DATA_WIDTH": 32,
    })

@pytest.mark.coverage
def test_GENERIC_MUX_4X1_stress_3_bits():
    GENERIC_MUX_4X1.test_with(tb_GENERIC_MUX_4X1_case_coverage_3_bits, {
        "DATA_WIDTH": 3,
    })


if __name__ == "__main__":
    lib.run_test(__file__)
