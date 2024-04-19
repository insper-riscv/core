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

    stage_if = CPU_STAGE_IF
    stage_id = CPU_STAGE_ID
    stage_ex = CPU_STAGE_EX
    stage_mem = CPU_STAGE_MEM
    stage_wb = CPU_STAGE_WB

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL(dut: CPU_TOP_LEVEL, trace: utils.Trace):
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
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR(dut: CPU_TOP_LEVEL, trace: utils.Trace):
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
        "00000000000000000000000000100000",
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
        yield trace.check(dut.stage_wb.destination, destination, f"At clock {index}.")

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_LINK_INSTRUCTIONS_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/LINK_INSTRUCTION_JAL.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/LINK_INSTRUCTION_JALR.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.test_with(
        testcase=[
            tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR
        ],
    )

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])