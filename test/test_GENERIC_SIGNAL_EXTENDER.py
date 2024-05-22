import pytest

import lib
from test_GENERICS_package import GENERICS
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class GENERIC_SIGNAL_EXTENDER(lib.Entity):
    _package = GENERICS

    source = lib.Entity.Input_pin
    enable_unsigned = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    MUX_UPPER = GENERIC_MUX_2X1


@pytest.mark.synthesis
def test_GENERIC_SIGNAL_EXTENDER_synthesis():
    GENERIC_SIGNAL_EXTENDER.build_vhd()
    GENERIC_SIGNAL_EXTENDER.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
