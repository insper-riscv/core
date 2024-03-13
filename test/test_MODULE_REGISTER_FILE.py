import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_SIGNAL_EXTENDER import GENERIC_SIGNAL_EXTENDER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_RV32I_REGISTER_FILE import RV32I_REGISTER_FILE


class MODULE_REGISTER_FILE(utils.DUT):
    CHILDREN = [GENERIC_SIGNAL_EXTENDER, GENERIC_ADDER, RV32I_REGISTER_FILE]


def test_MODULE_REGISTER_FILE_synthesis():
    MODULE_REGISTER_FILE.build_vhd()
    # MODULE_REGISTER_FILE.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
