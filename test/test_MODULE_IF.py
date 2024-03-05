from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_IF(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1, GENERIC_REGISTER, GENERIC_ADDER]


@cocotb.test()
async def tb_MODULE_IF(dut: MODULE_IF):
    pass


def test_MODULE_IF():
    MODULE_IF.test_with(tb_MODULE_IF)


if __name__ == "__main__":
    test_MODULE_IF()
