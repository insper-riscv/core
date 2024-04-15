import os
import subprocess

import pytest

import utils


class GENERICS(utils.VHD_Package):
    pass


@pytest.mark.synthesis
def test_GENERICS_package_synthesis():
    GENERICS.build_vhd()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
