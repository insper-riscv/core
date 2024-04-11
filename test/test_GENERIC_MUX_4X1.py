import os
import random

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERICS_package import GENERICS


class GENERIC_MUX_4X1(utils.DUT):
    _package = GENERICS

    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    source_3 = utils.DUT.Input_pin
    source_4 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin



@GENERIC_MUX_4X1.testcase
async def tb_GENERIC_MUX_4X1_case_1(dut: GENERIC_MUX_4X1, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000001")
    dut.source_2.value = BinaryValue("00000010")
    dut.source_3.value = BinaryValue("00000011")
    dut.source_4.value = BinaryValue("00000100")
    dut.selector.value = BinaryValue("00")

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
async def tb_GENERIC_MUX_4X1_case_stress(dut: GENERIC_MUX_4X1, trace: utils.Trace):
    for _ in range(250_000):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)
        source_3 = random.getrandbits(32)
        source_4 = random.getrandbits(32)
        selector = random.getrandbits(2)

        source_1_bits = utils.convert_to_binstr(source_1, 32)
        source_2_bits = utils.convert_to_binstr(source_2, 32)
        source_3_bits = utils.convert_to_binstr(source_3, 32)
        source_4_bits = utils.convert_to_binstr(source_4, 32)
        selector_bits = utils.convert_to_binstr(selector, 2)
    
        dut.source_1.value = BinaryValue(source_1_bits)
        dut.source_2.value = BinaryValue(source_2_bits)
        dut.source_3.value = BinaryValue(source_3_bits)
        dut.source_4.value = BinaryValue(source_4_bits)
        dut.selector.value = BinaryValue(selector_bits)
    
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
async def tb_GENERIC_MUX_4X1_case_stress_3_bits(dut: GENERIC_MUX_4X1, trace: utils.Trace):
    bits = 3
    for value_1 in range(2**bits):
        for value_2 in range(2**bits):
            for value_3 in range(2**bits):
                for value_4 in range(2**bits):
                    for selector in range(4):
                        source_1 = utils.convert_to_binstr(value_1, bits)
                        source_2 = utils.convert_to_binstr(value_2, bits)
                        source_3 = utils.convert_to_binstr(value_3, bits)
                        source_4 = utils.convert_to_binstr(value_4, bits)
                        selector = utils.convert_to_binstr(selector, 2)
                
                        dut.source_1.value = BinaryValue(source_1)
                        dut.source_2.value = BinaryValue(source_2)
                        dut.source_3.value = BinaryValue(source_3)
                        dut.source_4.value = BinaryValue(source_4)
                        dut.selector.value = BinaryValue(selector)

                        message = f"source_1: {source_1}, source_2: {source_2}, selector: {selector}"

                        await trace.cycle()

                        if selector == 0:  
                            yield trace.check(dut.destination, utils.convert_to_binstr(value_1, bits), message)
                        if selector == 1:  
                            yield trace.check(dut.destination, utils.convert_to_binstr(value_2, bits), message)
                        if selector == 2:  
                            yield trace.check(dut.destination, utils.convert_to_binstr(value_3, bits), message)
                        if selector == 3:  
                            yield trace.check(dut.destination, utils.convert_to_binstr(value_4, bits), message)

@pytest.mark.synthesis
def test_GENERIC_MUX_4X1_synthesis():
    GENERIC_MUX_4X1.build_vhd()
    GENERIC_MUX_4X1.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_MUX_4X1_testcases():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_1,
        ]
    )

@pytest.mark.stress
def test_GENERIC_MUX_4X1_stress():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_stress,
        ],
    )

@pytest.mark.stress
def test_GENERIC_MUX_4X1_stress_3_bits():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_stress_3_bits,
        ],
        parameters={"DATA_WIDTH": 3},
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
