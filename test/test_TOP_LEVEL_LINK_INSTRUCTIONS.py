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
async def tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000010001",
        "00000000000000000000000000011100",
        "00000000000000000000000000000000",
        "00000000000000000000000000001100",
        "00000000000000000000000000010000",
        "00000000000000000000000000010001",
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
async def tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR(dut: TOP_LEVEL, trace: lib.Waveform):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000011100",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000011100",
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
def test_TOP_LEVEL_LINK_INSTRUCTIONS_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/LINK_INSTRUCTION_JAL.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LINK_INSTRUCTION_JALR.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR
        ],
    )

    create_GENERIC_ROM(memory)

if __name__ == "__main__":
    lib.run_test(__file__)