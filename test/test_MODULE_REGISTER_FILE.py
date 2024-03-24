import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils
from test_RV32I_REGISTER_FILE import RV32I_REGISTER_FILE


class MODULE_REGISTER_FILE(utils.DUT):
    clock = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    select_destination = utils.DUT.Input_pin
    data_destination = utils.DUT.Input_pin
    instruction = utils.DUT.Input_pin
    data_source_1 = utils.DUT.Output_pin
    data_source_2 = utils.DUT.Output_pin

    register_file = RV32I_REGISTER_FILE

@cocotb.test()
@utils.append_wavedrom
async def tb_MODULE_REGISTER_FILE_case_1(dut: MODULE_REGISTER_FILE, trace: utils.Trace):
    values_select_destination = [
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
        "00001",
        "00011",
    ]
    values_instruction = [
        "0000000" + "00001" + "00000" + "000000000000000",
        "0000000" + "00011" + "00001" + "000000000000000",
        "0000000" + "00111" + "00011" + "000000000000000",
        "0000000" + "01111" + "00111" + "000000000000000",
        "0000000" + "11111" + "01111" + "000000000000000",
        "0000000" + "00000" + "11111" + "000000000000000",
        "0000000" + "00001" + "00000" + "000000000000000",
    ]
    values_data_destination = [
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
        "01111111111111111111111111111110",
        "11111111111111111000000000000000",
        "00000000000000001111111111111111",
    ]
    values_data_source_1 = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        values_data_destination[0],
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
    ]
    values_data_source_2 = [
        "00000000000000000000000000000000",
        values_data_destination[0],
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
        "00000000000000000000000000000000",
    ]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))
    await RisingEdge(dut.clock)

    for index, (
        select_destination,
        instruction,
        data_source_1,
        data_source_2,
        data_destination,
    ) in enumerate(
        zip(
            values_select_destination,
            values_instruction,
            values_data_source_1,
            values_data_source_2,
            values_data_destination,
        )
    ):
        dut.enable.value = BinaryValue("1")
        dut.select_destination.value = BinaryValue(select_destination)
        dut.instruction.value = BinaryValue(instruction)
        dut.data_destination.value = BinaryValue(data_destination)

        utils.assert_output(dut.data_source_1, data_source_1, f"At clock {index}.")
        utils.assert_output(dut.data_source_2, data_source_2, f"At clock {index}.")

        await RisingEdge(dut.clock)
        await Timer(Decimal(20000), units="ns")


def test_MODULE_REGISTER_FILE_synthesis():
    MODULE_REGISTER_FILE.build_vhd()
    # MODULE_REGISTER_FILE.build_netlistsvg()

def test_MODULE_REGISTER_FILE_testcases():
    MODULE_REGISTER_FILE.test_with(
        [
            tb_MODULE_REGISTER_FILE_case_1,
        ]
    )

if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
