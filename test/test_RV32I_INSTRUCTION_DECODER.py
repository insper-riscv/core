import os

import pytest
from cocotb.binary import BinaryValue

import utils


class RV32I_INSTRUCTION_DECODER(utils.DUT):
    instruction = utils.DUT.Input_pin
    control_if = utils.DUT.Output_pin
    control_id = utils.DUT.Output_pin
    control_ex = utils.DUT.Output_pin
    control_mem = utils.DUT.Output_pin
    control_wb = utils.DUT.Output_pin
    immediate = utils.DUT.Output_pin


@RV32I_INSTRUCTION_DECODER.testcase
async def tb_RV32I_INSTRUCTION_DECODER_case_1(dut: RV32I_INSTRUCTION_DECODER, trace: utils.Trace):
    values_instruction = [
        "11111111111100000000000000010011",
        "11111110000000000010111110100011",
        "11111110000000000000000001100011",
        "11111111111111111111000000110111",
        "11111111111000000000000001101111",
    ]
    values_immediate = [
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111011111100000",
        "11111111111111111111000000000000",
        "11111111111100000000011111111110",
    ]

    for index, (
        instruction,
        immediate,
    ) in enumerate(
        zip(
            values_instruction,
            values_immediate,
        )
    ):
        
        dut.instruction.value = BinaryValue(instruction)

        await trace.cycle()
        yield trace.check(dut.immediate, immediate, f"At clock {index}.")


def test_RV32I_INSTRUCTION_DECODER_synthesis():
    RV32I_INSTRUCTION_DECODER.build_vhd()
    # RV32I_INSTRUCTION_DECODER.build_netlistsvg()


def test_RV32I_INSTRUCTION_DECODER_testcases():
    RV32I_INSTRUCTION_DECODER.test_with(
        [
            tb_RV32I_INSTRUCTION_DECODER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
