import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

from utils_interpreter import *

import utils
from test_GENERIC_ROM import GENERIC_ROM
from test_GENERIC_RAM import GENERIC_RAM
from test_STAGE_IF import STAGE_IF
from test_STAGE_ID import STAGE_ID
from test_STAGE_EX import STAGE_EX
from test_STAGE_MEM import STAGE_MEM
from test_STAGE_WB import STAGE_WB


class TOP_LEVEL(utils.DUT):
    clock = utils.DUT.Input_pin
    data_program = utils.DUT.Input_pin
    data_memory_in = utils.DUT.Input_pin
    sw = utils.DUT.Input_pin
    data_memory_out = utils.DUT.Output_pin
    address_program = utils.DUT.Output_pin
    address_memory = utils.DUT.Output_pin
    memory_read = utils.DUT.Output_pin
    memory_write = utils.DUT.Output_pin
    led = utils.DUT.Output_pin

    rom = GENERIC_ROM
    ram = GENERIC_RAM
    stage_if = STAGE_IF
    stage_id = STAGE_ID
    stage_ex = STAGE_EX
    stage_mem = STAGE_MEM
    stage_wb = STAGE_WB


@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_LUI(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):
        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_AUIPC(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000001000000000000",
        "00000000000000000001000000000100",
        "00000000000000000001000000001000",
        "00000000000000000001000000001100",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):
        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ADDI(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ADD(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000001000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",#ainda sem hazard
        "00000000000000000000000000010000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_SUB(dut: TOP_LEVEL, trace: utils.Trace):
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
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_XOR(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000111",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_XORI(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_AND(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000111",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000100",
        "00000000000000000000000000000101",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ANDI(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000111",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_OR(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000000000000000000111",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ORI(dut: TOP_LEVEL, trace: utils.Trace):
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (destination, ) in enumerate(
        zip(values_destination)
    ):

        await trace.cycle()
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_SLL(dut: TOP_LEVEL, trace: utils.Trace):
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
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_SLLI(dut: TOP_LEVEL, trace: utils.Trace):
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
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@pytest.mark.synthesis
def test_TOP_LEVEL_synthesis():
    TOP_LEVEL.build_vhd()
    # TOP_LEVEL.build_netlistsvg()


@pytest.mark.testcases
def test_TOP_LEVEL_testcases():
    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    memory = "./src/GENERIC_ROM.vhd"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_LUI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_AUIPC.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_AUIPC
        ],
    )

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

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_AND.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_AND
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_ANDI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_ANDI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_OR.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_OR
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_ORI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_ORI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_XOR.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_XOR
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LOGICAL_INSTRUCTION_XORI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_XORI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SLL.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_SLL
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/SHIFT_INSTRUCTION_SLLI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.test_with(
        testcase=[
            tb_TOP_LEVEL_SLLI
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
