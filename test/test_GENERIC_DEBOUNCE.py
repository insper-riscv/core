from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_DEBOUNCE(utils.DUT):
    CHILDREN = [GENERIC_EDGE_DETECTOR, GENERIC_FLIP_FLOP]


@cocotb.test()
async def tb_GENERIC_DEBOUNCE(dut: GENERIC_DEBOUNCE):
    pass


def test_GENERIC_DEBOUNCE():
    GENERIC_DEBOUNCE.test_with(tb_GENERIC_DEBOUNCE)


if __name__ == "__main__":
    test_GENERIC_DEBOUNCE()
