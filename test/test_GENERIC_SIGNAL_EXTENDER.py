import pytest

import lib
from test_GENERICS_package import GENERICS


class GENERIC_SIGNAL_EXTENDER(lib.Device):
    _package = GENERICS

    source = lib.Device.Input_pin
    enable_unsigned = lib.Device.Input_pin
    destination = lib.Device.Output_pin


@pytest.mark.synthesis
def test_GENERIC_SIGNAL_EXTENDER_synthesis():
    GENERIC_SIGNAL_EXTENDER.build_vhd()
    # GENERIC_SIGNAL_EXTENDER.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
