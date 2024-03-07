from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PC(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1, GENERIC_REGISTER, GENERIC_ADDER]


@cocotb.test()
async def tb_MODULE_PC(dut: MODULE_PC):
    pass


def test_MODULE_PC():
    MODULE_PC.test_with(tb_MODULE_PC)


if __name__ == "__main__":
    test_MODULE_PC()
