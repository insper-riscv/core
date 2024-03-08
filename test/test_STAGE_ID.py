from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_REGISTERS_BANK import MODULE_REGISTERS_BANK
from test_MODULE_CONTROL_UNIT import MODULE_CONTROL_UNIT

class STAGE_ID(utils.DUT):
    CHILDREN = [MODULE_REGISTERS_BANK, MODULE_CONTROL_UNIT]


@cocotb.test()
async def tb_STAGE_ID(dut: STAGE_ID):
    pass


def test_STAGE_ID():
    STAGE_ID.test_with(tb_STAGE_ID)


if __name__ == "__main__":
    test_STAGE_ID()
