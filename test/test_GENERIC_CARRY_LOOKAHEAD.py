import pytest

import lib
from test_GENERICS_package import GENERICS


class GENERIC_CARRY_LOOKAHEAD(lib.Entity):
    _package = GENERICS

    carry_in = lib.Entity.Input_pin
    carry_generate = lib.Entity.Input_pin
    carry_propagate = lib.Entity.Input_pin
    carry_out = lib.Entity.Output_pin


@pytest.mark.synthesis
def test_GENERIC_CARRY_LOOKAHEAD_synthesis():
    GENERIC_CARRY_LOOKAHEAD.build_vhd()
    GENERIC_CARRY_LOOKAHEAD.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
