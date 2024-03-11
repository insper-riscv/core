from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils


class RV32I_REGISTER_FILE(utils.DUT):
    clock: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    address_destination: utils.DUT.Input_pin
    address_source_1: utils.DUT.Input_pin
    address_source_2: utils.DUT.Input_pin
    data_destination: utils.DUT.Input_pin
    data_source_1: utils.DUT.Output_pin
    data_source_2: utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_REGISTER_FILE_case_1(dut: RV32I_REGISTER_FILE):
    values_enable = ["1", "1", "1", "1", "1"]
    values_address_destination = [
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
    ]
    values_address_source_1 = [
        "00000",
        "00001",
        "00011",
        "00111",
        "01111",
    ]
    values_address_source_2 = [
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
    ]
    values_data_destination = [
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
        "01111111111111111111111111111110",
    ]
    values_data_source_1 = [
        "00000000000000000000000000000000",
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
    ]
    values_data_source_2 = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (
        enable,
        address_destination,
        address_source_1,
        address_source_2,
        data_destination,
        data_source_1,
        data_source_2,
    ) in enumerate(
        zip(
            values_enable,
            values_address_destination,
            values_address_source_1,
            values_address_source_2,
            values_data_destination,
            values_data_source_1,
            values_data_source_2,
        )
    ):
        dut.enable.value = BinaryValue(enable)
        dut.address_destination.value = BinaryValue(address_destination)
        dut.address_source_1.value = BinaryValue(address_source_1)
        dut.address_source_2.value = BinaryValue(address_source_2)
        dut.data_destination.value = BinaryValue(data_destination)

        await RisingEdge(dut.clock)
        await Timer(Decimal(20000), units="ns")
        utils.assert_output(dut.data_source_1, data_source_1, f"At clock {index}.")
        utils.assert_output(dut.data_source_2, data_source_2, f"At clock {index}.")


def test_RV32I_REGISTER_FILE_syntesis():
    RV32I_REGISTER_FILE.build_vhd()
    RV32I_REGISTER_FILE.build_netlistsvg()


def test_RV32I_REGISTER_FILE_case_1():
    RV32I_REGISTER_FILE.test_with(tb_RV32I_REGISTER_FILE_case_1)


if __name__ == "__main__":
    pytest.main(["-k", f"test_RV32I_REGISTER_FILE"])
