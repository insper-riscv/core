import os
import subprocess

import pytest

import utils


class RV32M(utils.VHD_Package):
    pass


@pytest.mark.synthesis
def test_RV32M_package_synthesis():
    RV32M.build_vhd()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
