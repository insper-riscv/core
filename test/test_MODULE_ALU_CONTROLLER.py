from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER


class MODULE_ALU_CONTROLLER(utils.DUT):
    CHILDREN = [RV32I_ALU_CONTROLLER]


@cocotb.test()
async def tb_MODULE_ALU_CONTROLLER(dut: MODULE_ALU_CONTROLLER):
    pass


def test_MODULE_ALU_CONTROLLER():
    MODULE_ALU_CONTROLLER.test_with(tb_MODULE_ALU_CONTROLLER)


if __name__ == "__main__":
    test_MODULE_ALU_CONTROLLER()
