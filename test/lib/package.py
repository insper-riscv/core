import typing as T
import subprocess


class Package():
    children: T.List[T.Type["Package"]] = []

    @classmethod
    def build_vhd(cls, timeout: int = 60):
        for child in cls.children:
            child.build_vhd(timeout)

        process = subprocess.Popen(
            [
                "ghdl",
                "-a",
                "--std=08",
                "--work=top",
                f"../src/{cls.__name__}.vhd",
            ],
            cwd="sim_build",
            stdout=subprocess.PIPE,
        )

        outs, errs = process.communicate(timeout=timeout)

        assert process.returncode == 0, outs.decode()
