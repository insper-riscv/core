from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_ROM(utils.DUT):
    address: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin

@cocotb.test()
async def tb_GENERIC_ROM_case_1(dut: "GENERIC_ROM"):
    dut.address.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "00000000000000000001010000110111")

    await Timer(Decimal(1), units="ns")

def test_GENERIC_ROM_synthesis():
    GENERIC_ROM.build_vhd()
    #GENERIC_ROM.build_netlistsvg()

def test_GENERIC_ROM_case_1():
    GENERIC_ROM.test_with(tb_GENERIC_ROM_case_1)


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_ROM"])
