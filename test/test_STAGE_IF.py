from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_PC import MODULE_PC


class STAGE_IF(utils.DUT):
    CHILDREN = [MODULE_PC]


@cocotb.test()
async def tb_STAGE_IF(dut: STAGE_IF):
    pass


def test_STAGE_IF():
    STAGE_IF.test_with(tb_STAGE_IF)


if __name__ == "__main__":
    test_STAGE_IF()
