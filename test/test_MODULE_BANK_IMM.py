from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_SIGNAL_EXTENDER import GENERIC_SIGNAL_EXTENDER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_REGISTERS_BANK import GENERIC_REGISTERS_BANK


class MODULE_BANK_IMM(utils.DUT):
    CHILDREN = [GENERIC_SIGNAL_EXTENDER, GENERIC_ADDER, GENERIC_REGISTERS_BANK]


@cocotb.test()
async def tb_MODULE_BANK_IMM(dut: MODULE_BANK_IMM):
    pass


def test_MODULE_BANK_IMM():
    MODULE_BANK_IMM.test_with(tb_MODULE_BANK_IMM)


if __name__ == "__main__":
    test_MODULE_BANK_IMM()
