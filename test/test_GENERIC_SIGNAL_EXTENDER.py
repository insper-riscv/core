from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_SIGNAL_EXTENDER(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_SIGNAL_EXTENDER(dut: GENERIC_SIGNAL_EXTENDER):
    pass


def test_GENERIC_SIGNAL_EXTENDER():
    GENERIC_SIGNAL_EXTENDER.build_vhd()
    GENERIC_SIGNAL_EXTENDER.test_with(tb_GENERIC_SIGNAL_EXTENDER)


if __name__ == "__main__":
    test_GENERIC_SIGNAL_EXTENDER()
