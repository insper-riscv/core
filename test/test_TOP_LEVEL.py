from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils
from test_STAGE_IF import STAGE_IF
from test_STAGE_ID import STAGE_ID
from test_STAGE_EX import STAGE_EX
from test_STAGE_MEM import STAGE_MEM
from test_STAGE_WB import STAGE_WB


class TOP_LEVEL(utils.DUT):
    CHILDREN = [STAGE_IF, STAGE_ID, STAGE_EX, STAGE_MEM, STAGE_WB]
    CLOCK       : utils.DUT.Input_pin
    SW          : utils.DUT.Input_pin
    LED         : utils.DUT.Output_pin
    destination : utils.DUT.Output_pin


@cocotb.test()
async def tb_TOP_LEVEL_case_1(dut: TOP_LEVEL):
    values_SW = ["0000", "0000", "0000", "0000", "0000"]

    values_LED = ["00000000", "00000000", "00000000", "00000000", "00000000"]

    values_destination = [
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
    ]

    clock = Clock(dut.CLOCK, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    for index, (t_SW, t_LED, destination) in enumerate(
        zip(values_SW, values_LED, values_destination)
    ):
        dut.SW.value = BinaryValue(t_SW)

        await RisingEdge(dut.CLOCK)
        utils.assert_output(dut.LED, t_LED, f"At clock {index}.")
        utils.assert_output(dut.destination, destination, f"At clock {index}.")
        await FallingEdge(dut.CLOCK)


def test_TOP_LEVEL_synthesis():
    TOP_LEVEL.build_vhd()
    #TOP_LEVEL.build_netlistsvg()


def test_TOP_LEVEL_case_1():
    TOP_LEVEL.test_with(tb_TOP_LEVEL_case_1)


if __name__ == "__main__":
    pytest.main(["-k", f"test_TOP_LEVEL"])
