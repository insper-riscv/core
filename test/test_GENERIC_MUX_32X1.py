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


@pytest.mark.synthesis
def test_GENERIC_MUX_32X1_synthesis():
    GENERIC_MUX_32X1.build_vhd()
    GENERIC_MUX_32X1.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
