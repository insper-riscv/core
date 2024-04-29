import pytest

import lib
from test_RV32I_package import RV32I


class RV32I_BRANCH_CONTROLLER(lib.Device):
    _package = RV32I

    select_function = lib.Device.Input_pin
    source_1 = lib.Device.Input_pin
    source_2 = lib.Device.Input_pin
    destination = lib.Device.Output_pin    



@pytest.mark.synthesis
def test_RV32I_BRANCH_CONTROLLER_synthesis():
    RV32I_BRANCH_CONTROLLER.build_vhd()
    # RV32I_BRANCH_CONTROLLER.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
