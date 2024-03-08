from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_WRITE_BACK import MODULE_WRITE_BACK


class STAGE_WB(utils.DUT):
    CHILDREN = [MODULE_WRITE_BACK]


@cocotb.test()
async def tb_STAGE_WB(dut: STAGE_WB):
    pass


def test_STAGE_WB():
    STAGE_WB.test_with(tb_STAGE_WB)


if __name__ == "__main__":
    test_STAGE_WB()
