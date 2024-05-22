import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_LOW_FREQ(lib.Entity):
    _package = GENERICS

    clock = lib.Entity.Input_pin
    clock_out = lib.Entity.Output_pin


@pytest.mark.synthesis
def test_GENERIC_LOW_FREQ_synthesis():
    GENERIC_LOW_FREQ.build_vhd()
    GENERIC_LOW_FREQ.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
