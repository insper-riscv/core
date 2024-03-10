from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_ROM import GENERIC_ROM


class MODULE_ROM(utils.DUT):
    CHILDREN = [GENERIC_ROM]


@cocotb.test()
async def tb_MODULE_ROM(dut: MODULE_ROM):
    pass


def test_MODULE_ROM():
    MODULE_ROM.test_with(tb_MODULE_ROM)


if __name__ == "__main__":
    test_MODULE_ROM()
