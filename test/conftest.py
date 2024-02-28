import subprocess
from pathlib import Path
import pytest

import utils


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    pass


def pytest_collect_file(path, parent):
    variables = {}

    with open(path, "r") as test_file:
        code = compile(test_file.read(), path, "exec")

        exec(code, variables)

    for variable in variables.values():
        if hasattr(variable, "__bases__") and issubclass(variable, utils.DUT):
            device: type[utils.DUT] = variable

            device.build_vhd()


def pytest_sessionstart(session: pytest.Session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    Path("sim_build").mkdir(exist_ok=True)
    subprocess.call(
        ["ghdl", "-a", "--work=top", "../src/TOP_LEVEL_CONSTANTS.vhd"], cwd="sim_build"
    )


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    pass


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
    pass
