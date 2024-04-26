import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERICS_package import GENERICS


class GENERIC_COMPARATOR(utils.DUT):
    _package = GENERICS

    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    flag_less = utils.DUT.Output_pin
    flag_greather = utils.DUT.Output_pin
    flag_equal = utils.DUT.Output_pin


@GENERIC_COMPARATOR.testcase
async def tb_GENERIC_COMPARATOR_case_1(dut: GENERIC_COMPARATOR, trace: utils.Trace):
    for source_1 in range(0, 4):
        for source_2 in range(0, 4):
            is_less = "1" if source_1 < source_2 else "0"
            is_greather = "1" if source_1 > source_2 else "0"
            is_equal = "1" if source_1 == source_2 else "0"
            dut.source_1.value = BinaryValue(utils.convert_to_binstr(source_1, 8), 8)
            dut.source_2.value = BinaryValue(utils.convert_to_binstr(source_2, 8), 8)

            await trace.cycle()
            yield trace.check(dut.flag_less, is_less, f"for {source_1} < {source_2}")
            yield trace.check(dut.flag_greather, is_greather, f"for {source_1} > {source_2}")
            yield trace.check(dut.flag_equal, is_equal, f"for {source_1} = {source_2}")

@pytest.mark.synthesis
def test_GENERIC_COMPARATOR_synthesis():
    GENERIC_COMPARATOR.build_vhd()
    # GENERIC_COMPARATOR.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_ADDER_testcases():
    GENERIC_COMPARATOR.test_with(
        [
            tb_GENERIC_COMPARATOR_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
