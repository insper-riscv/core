from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils


class GENERIC_REGISTER(utils.DUT):
    clock: utils.DUT.Input_pin
    clear: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_REGISTER(dut: GENERIC_REGISTER):
    clock = Clock(dut.clock, 20000, units="ns")
    values_clear = ['0', '0', '1', '0', '0']
    values_enable = ['1', '0', '0', '1', '1']
    values_source = ['11111111111111111111111111111111', '00000000000000000000000000000000', '00000000000000000000000000000000', '11111111111111111111111111111111', '00000000000000000000000000000000']
    values_destination = ['11111111111111111111111111111111', '11111111111111111111111111111111', '00000000000000000000000000000000', '11111111111111111111111111111111', '00000000000000000000000000000000']

    for index, (clear, enable, source, destination) in enumerate(zip(values_clear, values_enable, values_source, values_destination)):
        dut.clear.value =  BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)
        cocotb.start_soon(clock.start(start_high=False))

        await RisingEdge(dut.clock)

        await Timer(Decimal(20000), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(f"Expected value: {destination} Obtained value: {dut.destination.value.binstr}")

        assert condition, f"Error in test {index}: clear={clear} enable={enable} source={source} clock={clock}"
        await Timer(Decimal(20000), units="ns")


def test_GENERIC_REGISTER():
    GENERIC_REGISTER.build_vhd()
    GENERIC_REGISTER.test_with(tb_GENERIC_REGISTER)


if __name__ == "__main__":
    test_GENERIC_REGISTER()
