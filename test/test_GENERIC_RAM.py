from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_RAM(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_RAM(dut: GENERIC_RAM):
    pass


def test_GENERIC_RAM():
    GENERIC_RAM.test_with(tb_GENERIC_RAM)


if __name__ == "__main__":
    test_GENERIC_RAM()
