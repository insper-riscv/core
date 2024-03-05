from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_SIGNAL_EXTENDER import GENERIC_SIGNAL_EXTENDER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_REGISTERS_BANK import GENERIC_REGISTERS_BANK


class MODULE_ID(utils.DUT):
    CHILDREN = [GENERIC_SIGNAL_EXTENDER, GENERIC_ADDER, GENERIC_REGISTERS_BANK]


@cocotb.test()
async def tb_MODULE_ID(dut: MODULE_ID):
    pass


def test_MODULE_ID():
    MODULE_ID.test_with(tb_MODULE_ID)


if __name__ == "__main__":
    test_MODULE_ID()
