import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_RV32I_REGISTER_FILE import RV32I_REGISTER_FILE


class MODULE_REGISTER_FILE(lib.Entity):
    _package = MODULES

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    select_destination = lib.Entity.Input_pin
    select_source_1 = lib.Entity.Input_pin
    select_source_2 = lib.Entity.Input_pin
    data_destination = lib.Entity.Input_pin
    data_source_1 = lib.Entity.Output_pin
    data_source_2 = lib.Entity.Output_pin

    register_file = RV32I_REGISTER_FILE


@MODULE_REGISTER_FILE.testcase
async def tb_MODULE_REGISTER_FILE_case_1(dut: MODULE_REGISTER_FILE, trace: lib.Waveform):
    values_select_destination = [
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
        "00001",
        "00011",
    ]
    values_select_source_1 = [
        "00000",
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
        "00000",
    ]
    values_select_source_2 = [
        "00001",
        "00011",
        "00111",
        "01111",
        "11111",
        "00000",
        "00001",
    ]
    values_data_destination = [
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
        "01111111111111111111111111111110",
        "11111111111111111000000000000000",
        "00000000000000001111111111111111",
    ]
    values_data_source_1 = [
        "00000000000000000000000000000000",
        values_data_destination[0],
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
        "00000000000000000000000000000000",
    ]
    values_data_source_2 = [
        values_data_destination[0],
        values_data_destination[1],
        values_data_destination[2],
        values_data_destination[3],
        values_data_destination[4],
        "00000000000000000000000000000000",
        values_data_destination[5],
    ]

    for index, (
        select_destination,
        select_source_1,
        select_source_2,
        data_source_1,
        data_source_2,
        data_destination,
    ) in enumerate(
        zip(
            values_select_destination,
            values_select_source_1,
            values_select_source_2,
            values_data_source_1,
            values_data_source_2,
            values_data_destination,
        )
    ):
        dut.enable.value = BinaryValue("1")
        dut.select_destination.value = BinaryValue(select_destination)
        dut.select_source_1.value = BinaryValue(select_source_1)
        dut.select_source_2.value = BinaryValue(select_source_2)
        dut.data_destination.value = BinaryValue(data_destination)

        await trace.cycle()
        yield trace.check(dut.data_source_1, data_source_1, f"At clock {index}.")
        yield trace.check(dut.data_source_2, data_source_2, f"At clock {index}.")


@pytest.mark.synthesis
def test_MODULE_REGISTER_FILE_synthesis():
    MODULE_REGISTER_FILE.build_vhd()
    MODULE_REGISTER_FILE.build_netlistsvg()

@pytest.mark.testcases
def test_MODULE_REGISTER_FILE_testcases():
    MODULE_REGISTER_FILE.test_with(tb_MODULE_REGISTER_FILE_case_1)


if __name__ == "__main__":
    lib.run_test(__file__)
