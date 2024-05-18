import os
import random

import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_32X1(lib.Entity):
    _package = GENERICS

    selector = lib.Entity.Input_pin
    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    source_3 = lib.Entity.Input_pin
    source_4 = lib.Entity.Input_pin
    source_5 = lib.Entity.Input_pin
    source_6 = lib.Entity.Input_pin
    source_7 = lib.Entity.Input_pin
    source_8 = lib.Entity.Input_pin
    source_9 = lib.Entity.Input_pin
    source_10 = lib.Entity.Input_pin
    source_11 = lib.Entity.Input_pin
    source_12 = lib.Entity.Input_pin
    source_13 = lib.Entity.Input_pin
    source_14 = lib.Entity.Input_pin
    source_15 = lib.Entity.Input_pin
    source_16 = lib.Entity.Input_pin
    source_17 = lib.Entity.Input_pin
    source_18 = lib.Entity.Input_pin
    source_19 = lib.Entity.Input_pin
    source_20 = lib.Entity.Input_pin
    source_21 = lib.Entity.Input_pin
    source_22 = lib.Entity.Input_pin
    source_23 = lib.Entity.Input_pin
    source_24 = lib.Entity.Input_pin
    source_25 = lib.Entity.Input_pin
    source_26 = lib.Entity.Input_pin
    source_27 = lib.Entity.Input_pin
    source_28 = lib.Entity.Input_pin
    source_29 = lib.Entity.Input_pin
    source_30 = lib.Entity.Input_pin
    source_31 = lib.Entity.Input_pin
    source_32 = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_MUX_32X1.testcase
async def tb_GENERIC_MUX_32X1_coverage(dut: GENERIC_MUX_32X1, trace: lib.Waveform):
    for _ in range(5):
        pins = [f"source_{i}" for i in range(1, 33)]
        sources = [lib.to_binstr(random.getrandbits(8), 8) for _ in range(1, 33)]
        choice = random.randint(0, 31)
        selector = lib.to_binstr(choice, 5)
        destination = sources[choice]

        dut.selector.value = BinaryValue(selector)

        for key, value in zip(pins, sources):
            getattr(dut, key).value = BinaryValue(value)

        await trace.cycle(1)

        index = 0 #sources.index(dut.destination.value.binstr)
        message = f"Expected {pins[choice]} but got {pins[index]}."

        yield trace.check(dut.destination, destination, message)


@pytest.mark.synthesis
def test_GENERIC_MUX_32X1_synthesis():
    GENERIC_MUX_32X1.build_vhd()
    GENERIC_MUX_32X1.build_netlistsvg()


@pytest.mark.coverage
def test_GENERIC_MUX_32X1_coverage():
    GENERIC_MUX_32X1.test_with(tb_GENERIC_MUX_32X1_coverage)


if __name__ == "__main__":
    lib.run_test(__file__)
