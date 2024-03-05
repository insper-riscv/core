from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU_CONTROLLER(utils.DUT):
    pass


@cocotb.test()
async def tb_RV32I_ALU_CONTROLLER(dut: RV32I_ALU_CONTROLLER):
    pass


def test_RV32I_ALU_CONTROLLER():
    RV32I_ALU_CONTROLLER.test_with(tb_RV32I_ALU_CONTROLLER)


if __name__ == "__main__":
    test_RV32I_ALU_CONTROLLER()
