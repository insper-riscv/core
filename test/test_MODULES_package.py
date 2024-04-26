import os
import subprocess

import pytest

import utils
from test_CPU_package import CPU


class MODULES(utils.VHD_Package):
    children = [
        CPU
    ]


@pytest.mark.synthesis
def test_MODULES_package_synthesis():
    MODULES.build_vhd()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
