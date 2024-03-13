import subprocess
from pathlib import Path
import pytest


def pytest_sessionstart(session: pytest.Session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    Path("sim_build").mkdir(exist_ok=True)
    subprocess.call(
        ["ghdl", "-a", "--work=top", "../src/TOP_LEVEL_CONSTANTS.vhd"], cwd="sim_build"
    )
