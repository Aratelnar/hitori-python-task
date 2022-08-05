#!/usr/bin/env python3
import argparse
import sys

from coder import JsonCoder

parser = argparse.ArgumentParser(description="Hitori solver")
subparsers = parser.add_subparsers(title="Commands", dest='command')

parser_solve = subparsers.add_parser("solve", help="solve loaded puzzle")
parser_solve.add_argument('-f', '--file', nargs='?')

parser_load = subparsers.add_parser("load", help="load puzzle")
parser_load.add_argument('path')
parser_load.add_argument('format', nargs="?", default="json")

parser_save = subparsers.add_parser("save", help="save map as json")
parser_save.add_argument("path")

parser_exit = subparsers.add_parser("exit", help="exit command input")

def main(args=sys.argv[1:]):
    map = None
    while True:
        arg = parser.parse_args(args)
        if arg.command == 'solve':
            solve(arg, map)
        elif arg.command == 'load':
            map = load(arg.path, arg.format)
        elif arg.command == 'save':
            save(arg.path, map)
        elif arg.command == 'exit':
            return
        args = input("#> ").split(" ")


def solve(arg, map):
    if arg.file != None:
        map = load(arg.file)
    

def load(path, format="json"):
    with open(path, 'r') as f:
        if format == "json":
            return JsonCoder().decode_map(f.read())


def save(path, map):
    with open(path, "w") as f:
        data = JsonCoder().encode_map(map)
        f.write(data)


if __name__ == '__main__':
    main()
