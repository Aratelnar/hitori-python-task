from structures import *
from utilities import *
from coder import *


class ConnectivityRule:
    def check(self, map: Map) -> bool:
        checked = set()
        init = find_first_match(map, 1, None)
        queue = [init]
        while len(queue):
            item = queue.pop(0)
            for n in map.neighbours(item):
                if map[n].color != 0 and n not in checked:
                    queue.append(n)
            checked.add(item)
        b = True
        for i in map:
            if map[i].color != 0:
                b &= i in checked
        return b


class SummRule:
    def check(self, map: Map) -> bool:
        return True