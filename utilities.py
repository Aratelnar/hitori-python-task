from structures import *


def find_first_match(map: Map, *colors):
    found = False
    for coord in map:
        if map[coord].color in colors:
            found = True
            break
    return coord if found else None