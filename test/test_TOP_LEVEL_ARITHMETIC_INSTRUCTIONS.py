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
from test_CPU_LOAD_EXTENDER import CPU_LOAD_EXTENDER

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
    store_byte     = utils.DUT.Output_pin
    store_halfword = utils.DUT.Output_pin
    led = utils.DUT.Output_pin

    rom = GENERIC_ROM
    ram = GENERIC_RAM
    stage_if = STAGE_IF
    stage_id = STAGE_ID
    stage_ex = STAGE_EX
    stage_mem = STAGE_MEM
    stage_wb = STAGE_WB
    cpu_load_extender = CPU_LOAD_EXTENDER

@TOP_LEVEL.testcase
async def tb_TOP_LEVEL_ADDI(dut: TOP_LEVEL, trace: utils.Trace):
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

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])