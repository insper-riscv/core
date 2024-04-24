import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

from utils_interpreter import *

import utils
from test_CPU_package import CPU
from test_CPU_STAGE_IF import CPU_STAGE_IF
from test_CPU_STAGE_ID import CPU_STAGE_ID
from test_CPU_STAGE_EX import CPU_STAGE_EX
from test_CPU_STAGE_MEM import CPU_STAGE_MEM
from test_CPU_STAGE_WB import CPU_STAGE_WB

class CPU_TOP_LEVEL(utils.DUT):
    _package = CPU

    clock = utils.DUT.Input_pin
    data_program = utils.DUT.Input_pin
    data_memory_in = utils.DUT.Input_pin
    data_memory_out = utils.DUT.Output_pin
    address_program = utils.DUT.Output_pin
    address_memory = utils.DUT.Output_pin
    memory_read = utils.DUT.Output_pin
    memory_write = utils.DUT.Output_pin

    instruction_fetch = CPU_STAGE_IF
    instruction_decode = CPU_STAGE_ID
    execute = CPU_STAGE_EX
    memory_access = CPU_STAGE_MEM
    write_back = CPU_STAGE_WB

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLL(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000100000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000100000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLLI(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000010000000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
        "00000000000000000000000010000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRL(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000100000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRLI(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000100000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRA(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000100000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000001000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000001000000",
        "10000000000000000000000000000000",
        "11111110000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRAI(dut: CPU_TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000100000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000001000000000000",
        "00000000000000000000000001000000",
        "00000000000000000000000001000000",
        "10000000000000000000000000000000",
        "11111110000000000000000000000000",
        "11111110000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000001000000",
        "11111110000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.write_back.destination, destination, f"At clock {index}.")

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_SHIFT_INSTRUCTIONS_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SLL.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SLL
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SLLI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SLLI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SRL.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SRL
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SRLI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SRLI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SRA.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SRA
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SRAI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_SRAI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])