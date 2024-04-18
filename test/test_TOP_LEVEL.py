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

from test_TOP_LEVEL_ARITHMETIC_INSTRUCTIONS import tb_TOP_LEVEL_ADD, tb_TOP_LEVEL_ADDI, tb_TOP_LEVEL_SUB
from test_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_TOP_LEVEL_BGE, tb_TOP_LEVEL_BGEU, tb_TOP_LEVEL_BLT, tb_TOP_LEVEL_BLTU
from test_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_TOP_LEVEL_BEQ, tb_TOP_LEVEL_BNE
from test_TOP_LEVEL_BUILD_INSTRUCTIONS import tb_TOP_LEVEL_LUI, tb_TOP_LEVEL_AUIPC
from test_TOP_LEVEL_COMPARE_INSTRUCTIONS import tb_TOP_LEVEL_SLT, tb_TOP_LEVEL_SLTI, tb_TOP_LEVEL_SLTIU, tb_TOP_LEVEL_SLTU
from test_TOP_LEVEL_LINK_INSTRUCTIONS import tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL, tb_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR
from test_TOP_LEVEL_LOAD_INSTRUCTIONS import tb_TOP_LEVEL_LB, tb_TOP_LEVEL_LBU, tb_TOP_LEVEL_LH, tb_TOP_LEVEL_LHU, tb_TOP_LEVEL_LW
from test_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_TOP_LEVEL_AND, tb_TOP_LEVEL_ANDI, tb_TOP_LEVEL_OR, tb_TOP_LEVEL_ORI
from test_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_TOP_LEVEL_XOR, tb_TOP_LEVEL_XORI
from test_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_TOP_LEVEL_SLL, tb_TOP_LEVEL_SLLI, tb_TOP_LEVEL_SRA, tb_TOP_LEVEL_SRAI
from test_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_TOP_LEVEL_SRL, tb_TOP_LEVEL_SRLI
from test_TOP_LEVEL_STORE_INSTRUCTIONS import tb_TOP_LEVEL_SB, tb_TOP_LEVEL_SH, tb_TOP_LEVEL_SW


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

@pytest.mark.synthesis
def test_TOP_LEVEL_synthesis():
    TOP_LEVEL.build_vhd()
    # TOP_LEVEL.build_netlistsvg()


@pytest.mark.testcases
def test_TOP_LEVEL_testcases():
    memory = "./src/GENERIC_ROM.vhd"

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
