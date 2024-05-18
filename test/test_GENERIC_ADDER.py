import random

import pytest
from cocotb.binary import BinaryValue

import lib
from lib.utils import to_binstr as b
from test_GENERICS_package import GENERICS
from test_GENERIC_CARRY_LOOKAHEAD import GENERIC_CARRY_LOOKAHEAD


class GENERIC_ADDER(lib.Entity):
    _package = GENERICS

    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    carry_lookahead = GENERIC_CARRY_LOOKAHEAD


@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_case_1(dut: GENERIC_ADDER, trace: lib.Waveform):
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
async def tb_GENERIC_ADDER_coverage_case(dut: GENERIC_ADDER, trace: lib.Waveform):
    for _ in range(1_000_000):
        source_1 = random.getrandbits(8)
        source_2 = random.getrandbits(8)
    
        dut.source_1.value = BinaryValue(b(source_1, 8))
        dut.source_2.value = BinaryValue(b(source_2, 8))
    
        await trace.cycle()

        message = f"source_1: {b(source_1, 8)}, source_2: {b(source_2, 8)}"

        yield trace.check(dut.destination, b(source_1 + source_2, 8), message)


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


@pytest.mark.coverage
def test_GENERIC_ADDER_coverage():
    GENERIC_ADDER.test_with(
        [
            tb_GENERIC_ADDER_coverage_case
        ]
    )

#@pytest.mark.coverage
#def test_GENERIC_ADDER_stress_5_bits():
#    GENERIC_ADDER.test_with(
#        [
#            tb_GENERIC_ADDER_stress_5_bits,
#        ],
#        parameters={"DATA_WIDTH": 5},
#    )

if __name__ == "__main__":
    lib.run_test(__file__)
