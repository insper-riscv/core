from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_REGISTERS_BANK(utils.DUT):
    clock: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    address_destination: utils.DUT.Input_pin
    address_source_1: utils.DUT.Input_pin
    address_source_2: utils.DUT.Input_pin
    data_destination: utils.DUT.Input_pin
    data_source_1: utils.DUT.Output_pin
    data_source_2: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_REGISTERS_BANK(dut: GENERIC_REGISTERS_BANK):
    pass


def test_GENERIC_REGISTERS_BANK():
    GENERIC_REGISTERS_BANK.test_with(tb_GENERIC_REGISTERS_BANK)


if __name__ == "__main__":
    test_GENERIC_REGISTERS_BANK()
