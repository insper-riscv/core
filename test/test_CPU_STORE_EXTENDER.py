import pytest

import lib
from test_CPU_package import CPU


class CPU_STORE_EXTENDER(lib.Device):
    _package = CPU

    source = lib.Device.Input_pin
    selector = lib.Device.Input_pin
    destination = lib.Device.Output_pin

    output_1 = lib.Device.Output_pin


@pytest.mark.synthesis
def test_CPU_STORE_EXTENDER_synthesis():
    CPU_STORE_EXTENDER.build_vhd()
    # CPU_STORE_EXTENDER.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_STORE_EXTENDER_testcases():
    CPU_STORE_EXTENDER.test_with(
        [
            #tb_CPU_STORE_EXTENDER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
