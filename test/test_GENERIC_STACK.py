from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_STACK(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_STACK(dut: GENERIC_STACK):
    pass


def test_GENERIC_STACK():
    GENERIC_STACK.build_vhd()
    GENERIC_STACK.test_with(tb_GENERIC_STACK)


if __name__ == "__main__":
    test_GENERIC_STACK()
