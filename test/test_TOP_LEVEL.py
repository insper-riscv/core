import pytest

import lib
from test_GENERIC_ROM import GENERIC_ROM
from test_GENERIC_RAM import GENERIC_RAM
from test_CPU_TOP_LEVEL import CPU_TOP_LEVEL


class TOP_LEVEL(lib.Entity):
    clock = lib.Entity.Input_pin
    sw = lib.Entity.Input_pin
    led = lib.Entity.Output_pin

    ROM = GENERIC_ROM
    RAM = GENERIC_RAM
    CPU = CPU_TOP_LEVEL


@pytest.mark.synthesis
def test_TOP_LEVEL_synthesis():
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
