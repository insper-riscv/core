from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_SIGNAL_EXTENDER import GENERIC_SIGNAL_EXTENDER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_REGISTER_FILE import GENERIC_REGISTER_FILE


class MODULE_REGISTER_FILE(utils.DUT):
    CHILDREN = [GENERIC_SIGNAL_EXTENDER, GENERIC_ADDER, GENERIC_REGISTER_FILE]


@cocotb.test()
async def tb_MODULE_REGISTER_FILE(dut: MODULE_REGISTER_FILE):
    pass


def test_MODULE_REGISTER_FILE():
    MODULE_REGISTER_FILE.test_with(tb_MODULE_REGISTER_FILE)


if __name__ == "__main__":
    test_MODULE_REGISTER_FILE()
