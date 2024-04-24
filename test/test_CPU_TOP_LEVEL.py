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

from test_CPU_TOP_LEVEL_ARITHMETIC_INSTRUCTIONS import tb_CPU_TOP_LEVEL_ADD, tb_CPU_TOP_LEVEL_ADDI, tb_CPU_TOP_LEVEL_SUB
from test_CPU_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_CPU_TOP_LEVEL_BGE, tb_CPU_TOP_LEVEL_BGEU, tb_CPU_TOP_LEVEL_BLT, tb_CPU_TOP_LEVEL_BLTU
from test_CPU_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_CPU_TOP_LEVEL_BEQ, tb_CPU_TOP_LEVEL_BNE
from test_CPU_TOP_LEVEL_BUILD_INSTRUCTIONS import tb_CPU_TOP_LEVEL_LUI, tb_CPU_TOP_LEVEL_AUIPC
from test_CPU_TOP_LEVEL_COMPARE_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SLT, tb_CPU_TOP_LEVEL_SLTI, tb_CPU_TOP_LEVEL_SLTIU, tb_CPU_TOP_LEVEL_SLTU
from test_CPU_TOP_LEVEL_LINK_INSTRUCTIONS import tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL, tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR
from test_CPU_TOP_LEVEL_LOAD_INSTRUCTIONS import tb_CPU_TOP_LEVEL_LB, tb_CPU_TOP_LEVEL_LBU, tb_CPU_TOP_LEVEL_LH, tb_CPU_TOP_LEVEL_LHU, tb_CPU_TOP_LEVEL_LW
from test_CPU_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_CPU_TOP_LEVEL_AND, tb_CPU_TOP_LEVEL_ANDI, tb_CPU_TOP_LEVEL_OR, tb_CPU_TOP_LEVEL_ORI
from test_CPU_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_CPU_TOP_LEVEL_XOR, tb_CPU_TOP_LEVEL_XORI
from test_CPU_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SLL, tb_CPU_TOP_LEVEL_SLLI, tb_CPU_TOP_LEVEL_SRA, tb_CPU_TOP_LEVEL_SRAI
from test_CPU_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SRL, tb_CPU_TOP_LEVEL_SRLI
from test_CPU_TOP_LEVEL_STORE_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SB, tb_CPU_TOP_LEVEL_SH, tb_CPU_TOP_LEVEL_SW


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

    INSTRUCTION_FETCH = CPU_STAGE_IF
    INSTRUCTION_DECODE = CPU_STAGE_ID
    EXECUTE = CPU_STAGE_EX
    MEMORY_ACCESS = CPU_STAGE_MEM
    WRITE_BACK = CPU_STAGE_WB

@pytest.mark.synthesis
def test_CPU_TOP_LEVEL_synthesis():
    CPU_TOP_LEVEL.build_vhd()
    # CPU_TOP_LEVEL.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_TOP_LEVEL_testcases():
    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    memory = "./src/GENERIC_ROM.vhd"
    

    assembly = "./src/RV32I_INSTRUCTIONS/BUILD_INSTRUCTION_LUI.asm"
    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
