from structures import *
from utilities import *
from rules import *
from coder import *


def solve(imap: Map, coder):
    stack = [coder.encode_map(imap)]
    while len(stack):
        map = coder.decode_map(stack.pop())
        coord = find_first_match(map, None)
        if coord == None:
            yield map
            continue
        for c in [0,1]:
            res, m = solve_one(map, coord, c, coder)
            if res:
                stack.append(coder.encode_map(m))


def solve_one(imap: Map, coord, color, coder):
    map = coder.decode_map(coder.encode_map(imap))
    queue = [(coord, color)]
    checked = set()
    while len(queue):
        crd, col = queue.pop(0)
        cellCol = map[crd].color
        cellNum = map[crd].number
        if cellCol == None:
            map[crd].color = col
        elif cellCol != col:
            return False, imap
        
        if col == 1:
            for item in map.lines(crd):
                checkCell = map[item]
                if checkCell.number == cellNum and item in map and item not in checked and item != crd:
                    queue.append((item, 0))
        else:
            for item in map.neighbours(crd):
                queue.append((item, 1))
        checked.add(crd)
    res = check(map, ConnectivityRule(), SummRule())
    if not res:
        return False, imap
    return True, map


def check(map: Map, *rules):
    result = True
    for rule in rules:
        result &= rule.check(map)
    return result
