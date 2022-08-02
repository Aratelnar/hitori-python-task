#!/usr/bin/env python3
from coder import *
from solver import solve

with open("tests/rect/8x8.txt", 'r') as f:
    map = RectCoder().decode_map(f.read())

for m in solve(map, RectCoder()):
    print(RectCoder().encode_map(m))
    print()

with open("tests/hex/5.txt", 'r') as f:
    map = HexCoder().decode_map(f.read())

for m in solve(map, HexCoder()):
    print(HexCoder().encode_map(m))
