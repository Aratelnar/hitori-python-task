#!/usr/bin/env python3
import argparse
import sys
import solver

from coder import *

parser = argparse.ArgumentParser(description="Hitori solver")
subparsers = parser.add_subparsers(title="Commands", dest='command')

parser_solve = subparsers.add_parser("solve", help="solve loaded puzzle")
parser_solve.add_argument('-f', '--file', nargs='?')

parser_load = subparsers.add_parser("load", help="load puzzle")
parser_load.add_argument('path')
parser_load.add_argument('format', nargs="?", default="json")

parser_save = subparsers.add_parser("save", help="save map as json")
parser_save.add_argument('--index', '-i', type=int, nargs='?', default=None)
parser_save.add_argument("path")

parser_convert = subparsers.add_parser("convert", help="converts maps between formats")
parser_convert.add_argument("map_type")
parser_convert.add_argument("in_format")
parser_convert.add_argument("in_path")
parser_convert.add_argument("out_format")
parser_convert.add_argument("out_path")

parser_exit = subparsers.add_parser("exit", help="exit command input")

coders = {
    'rect': RectCoder(),
    'hex': HexCoder()
}

def main(args=sys.argv[1:]):
    map = None
    while True:
        arg = parser.parse_args(args)
        if arg.command == 'solve':
            solved = solve(arg, map)
        elif arg.command == 'load':
            map = load(arg.path, arg.format)
        elif arg.command == 'save':
            if arg.index == None:
                save(arg.path, map)
            else:
                save(arg.path, solved[arg.index])
        elif arg.command == 'convert':
            convert(arg)
        elif arg.command == 'exit':
            return
        args = input("#> ").split(" ")


def solve(arg, map):
    if arg.file != None:
        map = load(arg.file)
    return list(solver.solve(map))
    

def load(path, format="json"):
    with open(path, 'r') as f:
        if format == "json":
            return JsonCoder().decode_map(f.read())


def save(path, map):
    with open(path, "w") as f:
        data = JsonCoder().encode_map(map)
        f.write(data)


def convert(arg):
    with open(arg.in_path, 'r') as f:
        if arg.in_format == 'inner':
            data = coders[arg.map_type].decode_map(f.read())
        elif arg.in_format == 'json':
            data = JsonCoder().decode_map(f.read())

    with open(arg.out_path, 'w') as f:
        if arg.out_format == 'inner':
            f.write(coders[arg.map_type].encode_map(data))
        elif arg.out_format == 'json':
            f.write(JsonCoder().encode_map(data))


if __name__ == '__main__':
    main()
