import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_WRITE_BACK import MODULE_WRITE_BACK


class CPU_STAGE_WB(lib.Entity):
    _package = CPU

    source = lib.Entity.Input_pin
    enable_destination = lib.Entity.Output_pin
    select_destination = lib.Entity.Output_pin
    destination = lib.Entity.Output_pin

    module_write_back = MODULE_WRITE_BACK


@pytest.mark.synthesis
def test_CPU_STAGE_WB_synthesis():
    CPU_STAGE_WB.build_vhd()
    CPU_STAGE_WB.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
