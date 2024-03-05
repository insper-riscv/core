from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_WRITE_BACK(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1]


@cocotb.test()
async def tb_MODULE_WRITE_BACK(dut: MODULE_WRITE_BACK):
    pass


def test_MODULE_WRITE_BACK():
    MODULE_WRITE_BACK.test_with(tb_MODULE_WRITE_BACK)


if __name__ == "__main__":
    test_MODULE_WRITE_BACK()
