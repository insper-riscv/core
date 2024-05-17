import pytest

import lib
from test_RV32I_package import RV32I
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class RV32I_BRANCH_CONTROLLER(lib.Entity):
    _package = RV32I

    select_function = lib.Entity.Input_pin
    flag_sign_1 = lib.Entity.Input_pin
    flag_sign_2 = lib.Entity.Input_pin
    flag_equal = lib.Entity.Input_pin
    flag_less = lib.Entity.Input_pin
    flag_greather = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin   

    mux_case_beq = GENERIC_MUX_2X1
    mux_case_bne = GENERIC_MUX_2X1
    mux_case_blt = GENERIC_MUX_2X1
    mux_case_bge = GENERIC_MUX_2X1
    mux_case_bltu = GENERIC_MUX_2X1
    mux_case_bgeu = GENERIC_MUX_2X1



@pytest.mark.synthesis
def test_RV32I_BRANCH_CONTROLLER_synthesis():
    RV32I_BRANCH_CONTROLLER.build_vhd()
    RV32I_BRANCH_CONTROLLER.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
