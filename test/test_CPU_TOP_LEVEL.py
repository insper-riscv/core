import pytest
from cocotb.binary import BinaryValue

from utils_interpreter import *

import lib
from test_CPU_package import CPU
from test_CPU_STAGE_IF import CPU_STAGE_IF
from test_CPU_STAGE_ID import CPU_STAGE_ID
from test_CPU_STAGE_EX import CPU_STAGE_EX
from test_CPU_STAGE_MEM import CPU_STAGE_MEM
from test_CPU_STAGE_WB import CPU_STAGE_WB

#from test_CPU_TOP_LEVEL_ARITHMETIC_INSTRUCTIONS import tb_CPU_TOP_LEVEL_ADD, tb_CPU_TOP_LEVEL_ADDI, tb_CPU_TOP_LEVEL_SUB
#from test_CPU_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_CPU_TOP_LEVEL_BGE, tb_CPU_TOP_LEVEL_BGEU, tb_CPU_TOP_LEVEL_BLT, tb_CPU_TOP_LEVEL_BLTU
#from test_CPU_TOP_LEVEL_BRANCH_INSTRUCTIONS import tb_CPU_TOP_LEVEL_BEQ, tb_CPU_TOP_LEVEL_BNE
#from test_CPU_TOP_LEVEL_BUILD_INSTRUCTIONS import tb_CPU_TOP_LEVEL_LUI, tb_CPU_TOP_LEVEL_AUIPC
#from test_CPU_TOP_LEVEL_COMPARE_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SLT, tb_CPU_TOP_LEVEL_SLTI, tb_CPU_TOP_LEVEL_SLTIU, tb_CPU_TOP_LEVEL_SLTU
#from test_CPU_TOP_LEVEL_LINK_INSTRUCTIONS import tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JAL, tb_CPU_TOP_LEVEL_JUMP_INSTRUCTIONS_JALR
#from test_CPU_TOP_LEVEL_LOAD_INSTRUCTIONS import tb_CPU_TOP_LEVEL_LB, tb_CPU_TOP_LEVEL_LBU, tb_CPU_TOP_LEVEL_LH, tb_CPU_TOP_LEVEL_LHU, tb_CPU_TOP_LEVEL_LW
#from test_CPU_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_CPU_TOP_LEVEL_AND, tb_CPU_TOP_LEVEL_ANDI, tb_CPU_TOP_LEVEL_OR, tb_CPU_TOP_LEVEL_ORI
#from test_CPU_TOP_LEVEL_LOGICAL_INSTRUCTIONS import tb_CPU_TOP_LEVEL_XOR, tb_CPU_TOP_LEVEL_XORI
#from test_CPU_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SLL, tb_CPU_TOP_LEVEL_SLLI, tb_CPU_TOP_LEVEL_SRA, tb_CPU_TOP_LEVEL_SRAI
#from test_CPU_TOP_LEVEL_SHIFT_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SRL, tb_CPU_TOP_LEVEL_SRLI
#from test_CPU_TOP_LEVEL_STORE_INSTRUCTIONS import tb_CPU_TOP_LEVEL_SB, tb_CPU_TOP_LEVEL_SH, tb_CPU_TOP_LEVEL_SW


class CPU_TOP_LEVEL(lib.Entity):
    _package = CPU

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    data_program = lib.Entity.Input_pin
    data_memory_in = lib.Entity.Input_pin
    data_memory_out = lib.Entity.Output_pin
    address_program = lib.Entity.Output_pin
    address_memory = lib.Entity.Output_pin
    memory_read = lib.Entity.Output_pin
    memory_write = lib.Entity.Output_pin

    instruction_fetch = CPU_STAGE_IF
    instruction_decode = CPU_STAGE_ID
    execute = CPU_STAGE_EX
    memory_access = CPU_STAGE_MEM
    write_back = CPU_STAGE_WB


@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_case_1(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    address_values = [12, 24, 36]
    program = lib.Program("../test/data/c/test.c")

    dut.clear.value = BinaryValue("0")
    dut.enable.value = BinaryValue("1")
    dut.data_program.value = BinaryValue("00000000000000000000000000000000")
    dut.data_memory_in.value = BinaryValue("00000000000000000000000000000000")

    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield True

        assert address_values[index] == address, f"Invalid breakpoint address. At breakpoint {index}."

        if index > 2:
            break

@pytest.mark.synthesis
def test_CPU_TOP_LEVEL_synthesis():
    CPU_TOP_LEVEL.build_vhd()
    # CPU_TOP_LEVEL.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_TOP_LEVEL_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_case_1,
        ]
    )

if __name__ == "__main__":
    lib.run_test(__file__)
