import queue
from tabnanny import check
from structures import *


def solve(imap: Map):
    stack = [str(imap)]
    while len(stack):
        map = Map(data=stack.pop())
        coord = find_first_match(map, None)
        if coord == None:
            print(map)
            print()
            continue
        for c in [0,1]:
            res, m = solve_one(map, coord, c)
            if res:
                stack.append(str(m))


def solve_one(imap: Map, coord, color):
    map = Map(data=str(imap))
    queue = [(coord, color)]
    checked = set()
    while len(queue):
        crd, col = queue.pop(0)
        cellCol = map.data[crd[0]][crd[1]].color
        cellNum = map.data[crd[0]][crd[1]].number
        if cellCol == None:
            map.data[crd[0]][crd[1]].color = col
        elif cellCol != col:
            return False, imap
        
        if col == 1:
            for i in range(map.width):
                checkCell = map.data[crd[0]][i]
                if checkCell.number == cellNum and (crd[0], i) not in checked and i != crd[1]:
                    queue.append(((crd[0], i), 0))
            for i in range(map.height):
                checkCell = map.data[i][crd[1]]
                if checkCell.number == cellNum and (i, crd[1]) not in checked and i != crd[0]:
                    queue.append(((i, crd[1]), 0))
        else:
            for item in neighbours(crd, map):
                queue.append((item, 1))
        checked.add(crd)
    res = check(map)
    if not res:
        return False, imap
    return True, map


def check(map: Map):
    checked = set()
    init = find_first_match(map, 1, None)
    queue = [init]
    while len(queue):
        item = queue.pop(0)
        for n in neighbours(item, map):
            if map.data[n[0]][n[1]].color != 0 and n not in checked:
                queue.append(n)
        checked.add(item)
    b = True
    for i in range(map.height):
        for j in range(map.width):
            if map.data[i][j].color != 0:
                b &= (i, j) in checked
    return b


def neighbours(coord, map: Map):
    if coord[1] < map.width-1:
        yield coord[0], coord[1]+1
    if coord[1] > 0:
        yield coord[0], coord[1]-1
    if coord[0] < map.height-1:
        yield coord[0]+1, coord[1]
    if coord[0] > 0:
        yield coord[0]-1, coord[1]


def find_first_match(map: Map, *colors):
    found = False
    for row in range(map.height):
        if found:
            break
        for col in range(map.width):
            if map.data[row][col].color in colors:
                found = True
                coord = (row, col)
                break
    return coord if found else None


with open("tests/8x8.txt", 'r') as f:
    map = Map(data=f.read())

solve(map)
print(map)
