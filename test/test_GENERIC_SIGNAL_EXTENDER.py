from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_SIGNAL_EXTENDER(utils.DUT):
    source: utils.DUT.Input_pin
    enable_unsigned: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


def test_GENERIC_SIGNAL_EXTENDER_syntesis():
    GENERIC_SIGNAL_EXTENDER.build_vhd()
    GENERIC_SIGNAL_EXTENDER.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_SIGNAL_EXTENDER"])
