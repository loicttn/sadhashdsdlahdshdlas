#!/usr/bin/env python3

import sys
from tools.parser import Parser
from tools.solver import Solver


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        c = f.read().split("\n")
    p = Parser().run(c)
    Solver(p).run()
