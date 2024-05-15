import os
import random

import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_MUX_32X1(lib.Entity):
    _package = GENERICS

    selector = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
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
