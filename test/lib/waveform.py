import typing as T
import json

import cocotb.clock
import cocotb.triggers
import cocotb.wavedrom
import wavedrom
import pytest_check as check

from lib.clockless_trace import Clockless_Trace


class Waveform:
    def __init__(self, *args: T.Any, clock: T.Any, model: T.Optional["Device"] = None):
        self.clock = clock
        self.model = model

        if clock is not None:
            self._trace = cocotb.wavedrom.trace(*args, clk=clock)
            clock_ = cocotb.clock.Clock(clock, 20_000, units="ns")

            cocotb.start_soon(clock_.start(start_high=False))
        else:
            self._trace = Clockless_Trace(*args)

    def __enter__(self):
        self._trace.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._trace.__exit__(exc_type, exc_val, exc_tb)

    def disble(self):
        self._trace.disable()

    def enable(self):
        self._trace.enable()

    async def cycle(self, count: int = 1):
        if self.clock is not None:
            for _ in range(count):
                await cocotb.triggers.RisingEdge(self.clock)
                await cocotb.triggers.FallingEdge(self.clock)
        else:
            await cocotb.triggers.Timer(cocotb.triggers.Decimal(1), units="step")

    async def gap(self, count: int = 1):
        if count < 1:
            return

        self._trace.insert_gap()

        self._trace.disable()
        await self.cycle(count)
        self._trace.enable()

    def check(self, pin: T.Type["Device.Output_pin"], value: str, message: str = ""):
        result = check.equal(pin.value.binstr, value, f"At pin \"{pin._name}\". {message}")

        for signal in self._trace._signals:
            if pin._name not in signal._samples:
                continue

            signal._samples[pin._name][-1] = "7" if result else "9"

            if len(value) < 2:
                signal._data[pin._name].append(pin.value)

            break

        return result

    def write(self, filename: str):
        source = self._trace.dumpj()

        if self.model is not None:
            data = json.loads(source)
            inputs = self.model._get_input_pins()
            outputs = self.model._get_output_pins()
            index = 2

            data["signal"].insert(0, ["IN"])
            data["signal"].insert(1, ["OUT"])

            for signal in data["signal"][2:]:
                if signal["name"] in inputs:
                    data["signal"][0].append(data["signal"].pop(index))
                elif signal["name"] in outputs:
                    data["signal"][1].append(data["signal"].pop(index))
                else:
                    index += 1

            if len(data["signal"]) > 2:
                data["signal"].insert(2, {})

            source = json.dumps(data)

        drawing = wavedrom.render(source)

        if drawing is not None:
            return drawing.saveas(filename)

        raise ValueError("Invalid Wavedrom source!")


from lib.device import *
