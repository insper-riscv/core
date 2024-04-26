import os

import pytest

import utils
from test_GENERIC_ROM import GENERIC_ROM
from test_GENERIC_RAM import GENERIC_RAM
from test_CPU_TOP_LEVEL import CPU_TOP_LEVEL

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
    sw = utils.DUT.Input_pin
    led = utils.DUT.Output_pin

    rom = GENERIC_ROM
    ram = GENERIC_RAM
    cpu = CPU_TOP_LEVEL


@pytest.mark.synthesis
def test_TOP_LEVEL_synthesis():
    TOP_LEVEL.build_vhd()
    # TOP_LEVEL.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
