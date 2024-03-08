from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_INSTRUCTION_DECODER import RV32I_INSTRUCTION_DECODER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_CONTROL_UNIT(utils.DUT):
    CHILDREN = [RV32I_INSTRUCTION_DECODER, GENERIC_ADDER, GENERIC_MUX_2X1]


@cocotb.test()
async def tb_MODULE_CONTROL_UNIT(dut: MODULE_CONTROL_UNIT):
    pass


def test_MODULE_CONTROL_UNIT():
    MODULE_CONTROL_UNIT.test_with(tb_MODULE_CONTROL_UNIT)


if __name__ == "__main__":
    test_MODULE_CONTROL_UNIT()
