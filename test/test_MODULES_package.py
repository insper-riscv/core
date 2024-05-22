import pytest

import lib
from test_CPU_package import CPU


class MODULES(lib.Package):
    children = [
        CPU
    ]


@pytest.mark.synthesis
def test_MODULES_package_synthesis():
    MODULES.build_vhd()


if __name__ == "__main__":
    lib.run_test(__file__)
