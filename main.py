#!/usr/bin/env python3
import argparse
import sys

parser = argparse.ArgumentParser(description="Hitori solver")
subparsers = parser.add_subparsers(title="Commands", dest='command')

parser_solve = subparsers.add_parser("solve", help="solve loaded puzzle")
parser_solve.add_argument('-f', '--file', nargs='?')

parser_load = subparsers.add_parser("load", help="load puzzle")
parser_load.add_argument('path')


def main(args=sys.argv[1:]):
    arg = parser.parse_args(args)
    if arg.command == 'solve':
        solve(arg)
    elif arg.command == 'load':
        load(arg.path)


def solve(arg):
    if arg.file != None:
        load(arg.file)
    


def load(path):
    with open(path, 'r') as f:
        pass


if __name__ == '__main__':
    main()
