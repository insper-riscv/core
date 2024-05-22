import os
from pathlib import Path

import pytest


WORKSPACE_FOLDER = Path(__file__).parent.parent.absolute()


from lib.entity import Entity
from lib.package import Package
from lib.waveform import Waveform
from lib.clockless_trace import Clockless_Trace
from lib.program import Program
from lib.utils import *


def run_test(module: str):
    pytest.main(["-k", os.path.basename(module)])
