from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_BIT import RV32I_ALU_BIT


class RV32I_ALU(utils.DUT):
    CHILDREN = [RV32I_ALU_BIT]
    invert_source_1: utils.DUT.Input_pin
    invert_source_2: utils.DUT.Input_pin
    select_function: utils.DUT.Input_pin
    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin
    #flag_z: utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_ALU(dut: RV32I_ALU):
    values_invert_source_1 = ["0", "0", "0", "0", "1", "0", "1", "1",]
    values_invert_source_2 = ["0", "0", "0", "0", "0", "1", "0", "1",]
    values_select_function = ["00", "01", "10", "11", "00", "01", "10", "11",]
    values_source_1 = [
                        "00000000000000000000000000000000",
                        "11111111111111111111111111111111", 
                        "11111111111111110000000000000000", 
                        "11111111111111111111111111111111", 
                        "00000000000000000000000000000000", 
                        "11111111111111111111111111111111", 
                        "11111111111111110000000000000000", 
                        "11111111111111111111111111111111",
                       ]
    values_source_2 = [
                        "11111111111111111111111111111111", 
                        "00000000000000000000000000000000", 
                        "00000000000000001111111111111111", 
                        "00000000000000000000000000000000", 
                        "11111111111111111111111111111111", 
                        "00000000000000000000000000000000", 
                        "11111111111111110000000000000000",
                        "00000000000000000000000000000000",
                        ]
    values_destination = [
                            "00000000000000000000000000000000",
                            "11111111111111111111111111111111", 
                            "11111111111111111111111111111111", 
                            "00000000000000000000000000000001", 
                            "11111111111111111111111111111111", 
                            "11111111111111111111111111111111", 
                            "00000000000000000000000000000000", 
                            "00000000000000000000000000000001",
                          ]
    #values_flag_z = ["1", "0", "0", "0", "0", "0", "1", "0",]

    for index, (invert_source_1, invert_source_2, select_function,  source_1, source_2, 
            destination) in enumerate(
            #destination, flag_z) in enumerate(
        zip(values_invert_source_1, values_invert_source_2, values_select_function, 
            values_source_1, values_source_2, values_destination)
            #values_source_1, values_source_2, values_destination, values_flag_z)
    ):
        dut.invert_source_1.value = BinaryValue(invert_source_1)
        dut.invert_source_2.value = BinaryValue(invert_source_2)
        dut.select_function.value = BinaryValue(select_function)
        dut.source_1.value = BinaryValue(source_1)
        dut.source_2.value = BinaryValue(source_2)

        await Timer(Decimal(1), units="ns")

        condition = dut.destination.value.binstr == destination
        #condition1 = dut.flag_z.value.binstr == flag_z

        if not condition:
            dut._log.error(
                f"Expected destination value: {destination} Obtained value: {dut.destination.value.binstr}"
            )
        
        #if not condition1:
        #    dut._log.error(
        #        f"Expected flag_z value: {flag_z} Obtained value: {dut.flag_z.value.binstr}"
        #    )

        #assert (condition and condition1), f"Error in test {index}"
        assert (condition), f"Error in test {index}"
        await Timer(Decimal(1), units="ns")


def test_RV32I_ALU():
    RV32I_ALU.test_with(tb_RV32I_ALU)


if __name__ == "__main__":
    test_RV32I_ALU()
