from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_ROM(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_ROM(dut: GENERIC_ROM):
    pass


def test_GENERIC_ROM():
    GENERIC_ROM.test_with(tb_GENERIC_ROM)


if __name__ == "__main__":
    test_GENERIC_ROM()
