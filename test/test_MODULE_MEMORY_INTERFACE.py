import pytest

import lib
from test_MODULES_package import MODULES
from test_RV32I_TYPE_CONVERTER import RV32I_TYPE_CONVERTER


class MODULE_MEMORY_INTERFACE(lib.Entity):
    _package = MODULES

    select_function = lib.Entity.Input_pin
    source_data_in = lib.Entity.Input_pin
    source_data_out = lib.Entity.Input_pin
    destination_data_in = lib.Entity.Output_pin
    destination_data_out = lib.Entity.Output_pin

    DATA_IN = RV32I_TYPE_CONVERTER
    DATA_OUT = RV32I_TYPE_CONVERTER


@pytest.mark.synthesis
def test_MODULE_MEMORY_INTERFACE_synthesis():
    MODULE_MEMORY_INTERFACE.build_vhd()
    MODULE_MEMORY_INTERFACE.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
