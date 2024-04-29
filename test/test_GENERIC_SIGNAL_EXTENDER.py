import pytest

import lib
from test_GENERICS_package import GENERICS


class GENERIC_SIGNAL_EXTENDER(lib.Entity):
    _package = GENERICS

    source = lib.Entity.Input_pin
    enable_unsigned = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@pytest.mark.synthesis
def test_GENERIC_SIGNAL_EXTENDER_synthesis():
    GENERIC_SIGNAL_EXTENDER.build_vhd()
    # GENERIC_SIGNAL_EXTENDER.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
