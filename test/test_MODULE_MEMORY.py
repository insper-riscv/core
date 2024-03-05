from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_RAM import GENERIC_RAM


class MODULE_MEMORY(utils.DUT):
    CHILDREN = [GENERIC_RAM]


@cocotb.test()
async def tb_MODULE_MEMORY(dut: MODULE_MEMORY):
    pass


def test_MODULE_MEMORY():
    MODULE_MEMORY.test_with(tb_MODULE_MEMORY)


if __name__ == "__main__":
    test_MODULE_MEMORY()
