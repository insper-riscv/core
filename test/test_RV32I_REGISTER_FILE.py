import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils


class RV32I_REGISTER_FILE(utils.DUT):
    clock = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    address_destination = utils.DUT.Input_pin
    address_source_1 = utils.DUT.Input_pin
    address_source_2 = utils.DUT.Input_pin
    data_destination = utils.DUT.Input_pin
    data_source_1 = utils.DUT.Output_pin
    data_source_2 = utils.DUT.Output_pin

@RV32I_REGISTER_FILE.testcase
async def tb_RV32I_REGISTER_FILE_case_1(dut: RV32I_REGISTER_FILE, trace: utils.Trace):
    values_address_destination = [
        "00000",
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
        "00000",
    ]
    values_address_source_1 = [
        values_address_destination[6],
        values_address_destination[0],
        values_address_destination[1],
        values_address_destination[2],
        values_address_destination[3],
        values_address_destination[4],
        values_address_destination[5],
    ]
    values_address_source_2 = [
        values_address_destination[5],
        values_address_destination[6],
        values_address_destination[0],
        values_address_destination[1],
        values_address_destination[2],
        values_address_destination[3],
        values_address_destination[4],
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
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
        values_data_destination[5],
    ]
    values_data_source_2 = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
    ]
    clock = Clock(dut.clock, 2_000_000_000, units="fs")

    await cocotb.start(clock.start(start_high=False))

    for index, (
        address_destination,
        address_source_1,
        address_source_2,
        data_destination,
        data_source_1,
        data_source_2,
    ) in enumerate(
        zip(
            values_address_destination,
            values_address_source_1,
            values_address_source_2,
            values_data_destination,
            values_data_source_1,
            values_data_source_2,
        )
    ):
        dut.enable.value = BinaryValue("1")
        dut.address_destination.value = BinaryValue(address_destination)
        dut.address_source_1.value = BinaryValue(address_source_1)
        dut.address_source_2.value = BinaryValue(address_source_2)
        dut.data_destination.value = BinaryValue(data_destination)

        await trace.cycle()
        yield trace.check(dut.data_source_1, data_source_1, f"At clock {index}.")
        yield trace.check(dut.data_source_2, data_source_2, f"At clock {index}.")


def test_RV32I_REGISTER_FILE_synthesis():
    RV32I_REGISTER_FILE.build_vhd()
    # RV32I_REGISTER_FILE.build_netlistsvg()


def test_RV32I_REGISTER_FILE_testcases():
    RV32I_REGISTER_FILE.test_with(
        [
            tb_RV32I_REGISTER_FILE_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
