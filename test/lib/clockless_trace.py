import json

import cocotb.wavedrom
import cocotb.triggers


class Clockless_Trace(cocotb.wavedrom.trace):
    def __init__(self, *args):
        self._signals = []
        for arg in args:
            self._signals.append(cocotb.wavedrom.Wavedrom(arg))
        self._coro = None
        self._cycles = 0
        self._enabled = False

    async def _monitor(self):
        self._cycles = 0
        while True:
            await cocotb.triggers.ReadOnly()
            if not self._enabled:
                continue
            self._cycles += 1
            for sig in self._signals:
                sig.sample()

    def dumpj(self, header="", footer="", config=""):
        trace = {"signal": []}
        for sig in self._signals:
            trace["signal"].extend(sig.get(add_clock=False))
        if header:
            if isinstance(header, dict):
                trace["head"] = header
            else:
                trace["head"] = {"text": header}
        if footer:
            if isinstance(footer, dict):
                trace["foot"] = footer
            else:
                trace["foot"] = {"text": footer}
        if config:
            trace["config"] = config
        return json.dumps(trace, indent=4, sort_keys=False)
