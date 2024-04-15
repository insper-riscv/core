import os
import subprocess

import pytest

import utils
from test_RV32I_package import RV32I
from test_GENERICS_package import GENERICS


class CPU(utils.VHD_Package):
    children = [
        RV32I,
        GENERICS,
    ]

@pytest.mark.synthesis
def test_CPU_package_synthesis():
    CPU.build_vhd()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
