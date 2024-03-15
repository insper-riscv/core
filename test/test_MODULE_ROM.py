import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_ROM import GENERIC_ROM


class MODULE_ROM(utils.DUT):
    CHILDREN = [GENERIC_ROM]
    pc: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_MODULE_ROM_case_1(dut: "MODULE_ROM"):
    dut.pc.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "00000000000000000001010000110111")

    await Timer(Decimal(1), units="ns")


def test_MODULE_ROM_synthesis():
    MODULE_ROM.build_vhd()
    # MODULE_ROM.build_netlistsvg()


def test_MODULE_ROMGENERIC_ROM_testcases():
    MODULE_ROM.test_with(
        [
            tb_MODULE_ROM_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
