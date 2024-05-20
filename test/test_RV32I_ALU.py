import os
import random

import pytest
import random
from cocotb.binary import BinaryValue

import lib
from test_RV32I_package import RV32I
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1
from test_GENERIC_CARRY_LOOKAHEAD import GENERIC_CARRY_LOOKAHEAD
from test_RV32I_ALU_SHIFTER import RV32I_ALU_SHIFTER


operations = {
    "ADD":  "0000",
    "XOR":  "0100",
    "OR":   "0110",
    "AND":  "0111",
    "SUB":  "1000", 
    "SLL":  "0001",
    "SLT":  "0010",
    "SLTU": "0011",
    "SRL":  "0101",
    "SRA":  "1101",
    }

class RV32I_ALU(lib.Entity):
    _package = RV32I

    select_function = lib.Entity.Input_pin
    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    overflow = lib.Entity.Output_pin
    destination = lib.Entity.Output_pin

    mux_source_2 = GENERIC_MUX_2X1
    carry_lookahead = GENERIC_CARRY_LOOKAHEAD
    shifter = RV32I_ALU_SHIFTER
    mux_destination_1 = GENERIC_MUX_4X1
    mux_destination_2 = GENERIC_MUX_4X1
    mux_destination_3 = GENERIC_MUX_2X1


@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_1(dut: RV32I_ALU, trace: lib.Waveform):
    
    #AND
    dut.select_function.value = BinaryValue("0111")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    trace.set_scale(2)
    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 0")

    dut.select_function.value = BinaryValue("0111")
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    trace.set_scale(2)
    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 0")

    dut.select_function.value = BinaryValue("0110") # 000001
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 1")

    dut.select_function.value = BinaryValue("0000") # 000011
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("00000000000000001111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 2")

    dut.select_function.value = BinaryValue("1011") # 110111
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 3")

    dut.select_function.value = BinaryValue("1000") # 001000
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001", "At 4")

    dut.select_function.value = BinaryValue("1110") # 010001
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111", "At 5")

    dut.select_function.value = BinaryValue("1000") # 001011
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("11111111111111110000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000", "At 6")

    dut.select_function.value = BinaryValue("1010") # 010111
    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000100")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001", "At 7")

    dut.select_function.value = BinaryValue("0001") # 000100
    dut.source_1.value = BinaryValue("00000000000000000000000000001000")
    dut.source_2.value = BinaryValue("00000000000000000000000000001000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000100000000000", "At 8")

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_and(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 100_000
    dut.select_function.value = BinaryValue(operations["AND"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 & source_2, 32))

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_or(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50_000
    dut.select_function.value = BinaryValue(operations["OR"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 | source_2, 32))

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_xor(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50_000
    dut.select_function.value = BinaryValue(operations["XOR"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 ^ source_2, 32))

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_add(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50_000
    dut.select_function.value = BinaryValue(operations["ADD"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 + source_2, 32)[-32:])

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_sub(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50_000
    dut.select_function.value = BinaryValue(operations["SUB"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        expected = '{0:0{1}b}'.format((source_1-source_2) & (2**32 - 1), 32) if source_1 < source_2 else '{0:0{1}b}'.format(source_1-source_2, 32)

        await trace.cycle()
        yield trace.check(dut.destination, expected)

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_sll(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50_000
    dut.select_function.value = BinaryValue(operations["SLL"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(5)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))


        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 << source_2, 32)[-32:])

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_slt(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50
    dut.select_function.value = BinaryValue(operations["SLT"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(31)
        source_2 = random.getrandbits(31)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        message = f"source_1: {'{0:0{1}b}'.format(source_1, 32)} source_2: {'{0:0{1}b}'.format(source_2, 32)} expected: {1 if source_1 < source_2 else 0}"

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(1 if source_1 < source_2 else 0, 32), message)


@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_sltu(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50
    dut.select_function.value = BinaryValue(operations["SLTU"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        message = f"source_1: {'{0:0{1}b}'.format(source_1, 32)} source_2: {'{0:0{1}b}'.format(source_2, 32)} expected: {1 if source_1 < source_2 else 0}"

        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(1 if source_1 < source_2 else 0, 32), message)

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_srl(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50
    dut.select_function.value = BinaryValue(operations["SRL"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(5)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))


        await trace.cycle()
        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1 >> source_2, 32))

@RV32I_ALU.testcase
async def tb_RV32I_ALU_case_coverage_sra(dut: RV32I_ALU, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 50
    dut.select_function.value = BinaryValue(operations["SRA"])

    for _ in range(qnt_tests):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(5)

        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))

        expected = '{0:0{1}b}'.format(source_1 >> source_2, 32-source_2)
        expected = expected[0]*source_2 + expected

        message = f"Shift: {'{0:0{1}b}'.format(source_1 >> source_2, 32-source_2)} Source_1: {'{0:0{1}b}'.format(source_1, 32)} Source_2: {source_2} Expected: {expected}" 

        await trace.cycle()
        yield trace.check(dut.destination, expected, message)


@pytest.mark.synthesis
def test_RV32I_ALU_synthesis():
    RV32I_ALU.build_vhd()
    RV32I_ALU.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_testcases():
    RV32I_ALU.test_with(tb_RV32I_ALU_case_1)

@pytest.mark.coverage
def test_RV32I_ALU_stress():
    RV32I_ALU.test_with(
        [
            tb_RV32I_ALU_case_coverage_and,
            tb_RV32I_ALU_case_coverage_or,
            tb_RV32I_ALU_case_coverage_xor,
            tb_RV32I_ALU_case_coverage_add,
            tb_RV32I_ALU_case_coverage_sub,
            tb_RV32I_ALU_case_coverage_sll,
            tb_RV32I_ALU_case_coverage_srl,
            tb_RV32I_ALU_case_coverage_sra,
        ],
    )


if __name__ == "__main__":
    lib.run_test(__file__)
