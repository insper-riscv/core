from email import message
import os
import random

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils
from test_GENERICS_package import GENERICS


class GENERIC_REGISTER(utils.DUT):
    _package = GENERICS

    clock = utils.DUT.Input_pin
    clear = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_1(dut: GENERIC_REGISTER, trace: utils.Trace):
    values_clear = ["0", "0", "1", "0", "0"]
    values_enable = ["1", "0", "0", "1", "1"]
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
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (clear, enable, source, destination) in enumerate(
        zip(values_clear, values_enable, values_source, values_destination)
    ):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_stress(dut: GENERIC_REGISTER, trace: utils.Trace):
    qnt_tests = 30_000
    
    clear = "0"
    enable = "1"
    
    clock = Clock(dut.clock, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))
    
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
async def tb_GENERIC_REGISTER_case_stress_15_bits(dut: GENERIC_REGISTER, trace: utils.Trace):
    bits = 15
    
    clear = "0"
    enable = "1"

    clock = Clock(dut.clock, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

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
    GENERIC_REGISTER.test_with(
        [
            tb_GENERIC_REGISTER_case_1,
        ]
    )

@pytest.mark.stress
def test_GENERIC_REGISTER_stress():
    GENERIC_REGISTER.test_with(
        [
            tb_GENERIC_REGISTER_case_stress,
        ],
         parameters={"DATA_WIDTH": 32},
    )

@pytest.mark.stress
def test_GENERIC_REGISTER_stress_15_bits():
    GENERIC_REGISTER.test_with(
        [
            tb_GENERIC_REGISTER_case_stress_15_bits,
        ],
        parameters = {'DATA_WIDTH': 15}
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
