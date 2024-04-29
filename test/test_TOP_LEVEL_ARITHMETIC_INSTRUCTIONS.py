import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

from utils_interpreter import *
from utils_GENERIC_ROM import *

import lib
from test_GENERIC_ROM import GENERIC_ROM
from test_GENERIC_RAM import GENERIC_RAM
from test_CPU_TOP_LEVEL import CPU_TOP_LEVEL


class TOP_LEVEL(lib.Device):
    clock = lib.Device.Input_pin
    sw = lib.Device.Input_pin
    led = lib.Device.Output_pin

    rom = GENERIC_ROM
    ram = GENERIC_RAM
    cpu = CPU_TOP_LEVEL

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ADDI(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000001",
        "00000000000000000000000000000010",
        "00000000000000000000000000000100",
        "00000000000000000000000000001000",
        "00000000000000000000000000010000",
        "00000000000000000000000000100000",
        "00000000000000000000000001000000",
        "00000000000000000000000010000000",
        "00000000000000000000000100000000",
        "00000000000000000000000100000001",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.cpu.write_back.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ADD(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",#ainda sem hazard
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.cpu.write_back.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_SUB(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000000000000000010",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.cpu.write_back.destination, destination, f"At clock {index}.")

@pytest.mark.testcases
def test_TOP_LEVEL_ARITHMETIC_INSTRUCTIONS_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/ARITHMETIC_INSTRUCTION_ADD.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_ADD
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/ARITHMETIC_INSTRUCTION_ADDI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_ADDI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/ARITHMETIC_INSTRUCTION_SUB.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_SUB
        ],
    )

    create_GENERIC_ROM(memory)

if __name__ == "__main__":
    lib.run_test(__file__)