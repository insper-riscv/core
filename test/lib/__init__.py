import os

import pytest

from lib.device import Device
from lib.package import Package
from lib.waveform import Waveform
from lib.clockless_trace import Clockless_Trace
from lib.program import Program
from lib.utils import *

def run_test(module: str):
    pytest.main(["-k", os.path.basename(module)])
