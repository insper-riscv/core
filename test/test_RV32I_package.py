import os
import subprocess

import pytest

import utils
from test_GENERICS_package import GENERICS


class RV32I(utils.VHD_Package):
    children = [
        GENERICS
    ]


@pytest.mark.synthesis
def test_RV32I_package_synthesis():
    RV32I.build_vhd()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
