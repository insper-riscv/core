from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_MEMORY import MODULE_MEMORY


class STAGE_MEM(utils.DUT):
    CHILDREN = [MODULE_MEMORY]


@cocotb.test()
async def tb_STAGE_MEM(dut: STAGE_MEM):
    pass


def test_STAGE_MEM():
    STAGE_MEM.test_with(tb_STAGE_MEM)


if __name__ == "__main__":
    test_STAGE_MEM()
