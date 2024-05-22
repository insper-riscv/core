from email import message
import os
import random

import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_REGISTER(lib.Entity):
    _package = GENERICS

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_1(dut: GENERIC_REGISTER, trace: lib.Waveform):
    values_enable = ["1", "0", "1", "1", "1"]
    values_clear = ["0", "0", "1", "0", "0"]
    values_source = [
        "11111111",
        "00000000",
        "00000000",
        "11111111",
        "00000000",
    ]
    values_destination = [
        "11111111",
        "11111111",
        "00000000",
        "11111111",
        "00000000",
    ]

    yield trace.check(dut.destination, "00000000", "At clock 0.")

    for index, (clear, enable, source, destination) in enumerate(
        zip(values_clear, values_enable, values_source, values_destination),
        1,
    ):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")

@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_coverage(dut: GENERIC_REGISTER, trace: lib.Waveform):
    trace.disable()

    qnt_tests = 30_000
    clear = "0"
    enable = "1"

    for _ in range(qnt_tests):
        source = random.getrandbits(32)

        source_bits = '{0:0{1}b}'.format(source, 32)
        destination = source_bits

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)

    source = random.getrandbits(32)
    source_bits = '{0:0{1}b}'.format(source, 32)
    destination = source_bits

    dut.clear.value = BinaryValue(clear)
    dut.enable.value = BinaryValue(enable)
    dut.source.value = BinaryValue(source_bits)

    await trace.cycle()

    enable = "0"

    for _ in range(qnt_tests):
        source = random.getrandbits(32)

        source_bits = '{0:0{1}b}'.format(source, 32)

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)

    clear = "1"
    enable = "0"
    destination = '{0:0{1}b}'.format(0, 32)

    for _ in range(qnt_tests):
        source = random.getrandbits(32)

        source_bits = '{0:0{1}b}'.format(source, 32)

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)

@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_coverage_15_bits(dut: GENERIC_REGISTER, trace: lib.Waveform):
    trace.disable()

    bits = 15
    clear = "0"
    enable = "1"

    for source in range(2**bits):
        source_bits = '{0:0{1}b}'.format(source, bits)
        destination = source_bits

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)


    source = random.getrandbits(bits)
    source_bits = '{0:0{1}b}'.format(source, bits)
    destination = source_bits

    dut.clear.value = BinaryValue(clear)
    dut.enable.value = BinaryValue(enable)
    dut.source.value = BinaryValue(source_bits)

    await trace.cycle()

    enable = "0"

    for source in range(2**bits):
        source_bits = '{0:0{1}b}'.format(source, bits)

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)

    clear = "1"
    enable = "0"
    destination = '{0:0{1}b}'.format(0, bits)

    for source in range(2**bits):
        source_bits = '{0:0{1}b}'.format(source, bits)

        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source_bits)

        message = f"Enable: {enable}, Clear: {clear}, Source: {source_bits}, Destination: {destination}"

        await trace.cycle()
        yield trace.check(dut.destination, destination, message)


@pytest.mark.synthesis
def test_GENERIC_REGISTER_synthesis():
    GENERIC_REGISTER.build_vhd()
    GENERIC_REGISTER.build_netlistsvg()

@pytest.mark.testcases
def test_GENERIC_REGISTER_testcases():
    GENERIC_REGISTER.test_with(tb_GENERIC_REGISTER_case_1)

@pytest.mark.coverage
def test_GENERIC_REGISTER_stress():
    GENERIC_REGISTER.test_with(tb_GENERIC_REGISTER_case_coverage, {
        "DATA_WIDTH": 32,
    })

@pytest.mark.coverage
def test_GENERIC_REGISTER_stress_15_bits():
    GENERIC_REGISTER.test_with(tb_GENERIC_REGISTER_case_coverage_15_bits, {
        "DATA_WIDTH": 15,
    })


if __name__ == "__main__":
    lib.run_test(__file__)
