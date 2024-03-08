from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_ALU import MODULE_ALU


class STAGE_EX(utils.DUT):
    CHILDREN = [MODULE_ALU]


@cocotb.test()
async def tb_STAGE_EX(dut: STAGE_EX):
    pass


def test_STAGE_EX():
    STAGE_EX.test_with(tb_STAGE_EX)


if __name__ == "__main__":
    test_STAGE_EX()
