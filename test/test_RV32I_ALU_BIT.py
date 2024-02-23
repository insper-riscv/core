from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU_BIT(utils.DUT):
    invert_source_1: utils.DUT.Input_pin
    invert_source_2: utils.DUT.Input_pin
    select_function: utils.DUT.Input_pin
    carry_in: utils.DUT.Input_pin
    slt: utils.DUT.Input_pin
    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin
    carry_out: utils.DUT.Output_pin
    overflow: utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_ALU_BIT(dut: RV32I_ALU_BIT):
    values_invert_source_1 = ["0", "0", "0", "0", "1", "1", "1", "1",]
    values_invert_source_2 = ["0", "0", "0", "0", "1", "1", "1", "1",]
    values_select_function = ["00", "01", "10", "11", "00", "01", "10", "11",]
    values_carry_in = ["0", "0", "1", "1", "0", "0", "1", "1",]
    values_slt = ["0", "0", "0", "1", "0", "0", "0", "1",]
    values_source_1 = ["0", "1", "0", "1", "0", "1", "0", "1",]
    values_source_2 = ["1", "0", "1", "0", "1", "0", "1", "0",]
    values_destination = ["0", "1", "0", "1", "0", "1", "0", "1",]
    values_carry_out = ["0", "0", "1", "1", "0", "0", "1", "1",]
    values_overflow = ["1", "1", "0", "0", "1", "1", "0", "0",]

    for index, (invert_source_1, invert_source_2, select_function, 
            carry_in, slt, source_1, source_2, 
            destination, carry_out, overflow) in enumerate(
        zip(values_invert_source_1, values_invert_source_2, values_select_function, 
            values_carry_in, values_slt, values_source_1, values_source_2, 
            values_destination, values_carry_out, values_overflow)
    ):
        dut.invert_source_1.value = BinaryValue(invert_source_1)
        dut.invert_source_2.value = BinaryValue(invert_source_2)
        dut.select_function.value = BinaryValue(select_function)
        dut.carry_in.value = BinaryValue(carry_in)
        dut.slt.value = BinaryValue(slt)
        dut.source_1.value = BinaryValue(source_1)
        dut.source_2.value = BinaryValue(source_2)

        await Timer(Decimal(1), units="ns")

        condition = dut.destination.value.binstr == destination
        condition1 = dut.carry_out.value.binstr == carry_out
        condition2 = dut.overflow.value.binstr == overflow

        if not condition:
            dut._log.error(
                f"Expected destination value: {destination} Obtained value: {dut.destination.value.binstr}"
            )

        if not condition1:
            dut._log.error(
                f"Expected carry_out value: {carry_out} Obtained value: {dut.carry_out.value.binstr}"
            )
        
        if not condition2:
            dut._log.error(
                f"Expected overflow value: {overflow} Obtained value: {dut.overflow.value.binstr}"
            )

        assert (condition and condition1 and condition2), f"Error in test {index}"
        await Timer(Decimal(1), units="ns")


def test_RV32I_ALU_BIT():
    RV32I_ALU_BIT.test_with(tb_RV32I_ALU_BIT)


if __name__ == "__main__":
    test_RV32I_ALU_BIT()
