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


class TOP_LEVEL(lib.Entity):
    clock = lib.Entity.Input_pin
    sw = lib.Entity.Input_pin
    led = lib.Entity.Output_pin

    rom = GENERIC_ROM
    ram = GENERIC_RAM
    cpu = CPU_TOP_LEVEL

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_BEQ(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
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
async def tb_TOP_LEVEL_BNE(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
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
async def tb_TOP_LEVEL_BLT(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
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
async def tb_TOP_LEVEL_BLTU(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
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
async def tb_TOP_LEVEL_BGE(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
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
async def tb_TOP_LEVEL_BGEU(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
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
def test_TOP_LEVEL_BRANCH_INSTRUCTIONS_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BEQ.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BEQ
        ],
    )
    
    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BNE.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BNE
        ],
    )
    
    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BLT.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BLT
        ],
    )
    
    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BLTU.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BLTU
        ],
    )
    
    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BGE.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BGE
        ],
    )
    
    assembly = "./src/RV32I_INSTRUCTIONS/BRANCH_INSTRUCTION_BGEU.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_BGEU
        ],
    )

    create_GENERIC_ROM(memory)

if __name__ == "__main__":
    lib.run_test(__file__)