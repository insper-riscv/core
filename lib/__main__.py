import argparse
from pathlib import Path

import lib


parser = argparse.ArgumentParser(description="Parse program into Memory Initialization File (.mif)")

parser.add_argument("entry", type=Path, help="Entry .c or .S program file")
parser.add_argument("-o", "--output", type=Path, default=None, help="Output file")
parser.add_argument("-d", "--depth", type=int, default=128, help="Memory depth")

args = parser.parse_args()
program = lib.Program(args.entry)

if args.output is None:
    args.output = args.entry.with_suffix(".mif")

args.output.parent.mkdir(parents=True, exist_ok=True)

with open(args.output, "w") as output_file:
    output = program.to_memory_initialization_file(32, args.depth)

    output_file.write(output)
