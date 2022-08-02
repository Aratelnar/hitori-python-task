import copy


class Map:
    def __init__(self, data) -> None:
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, coord):
        return self.data[coord]

    def neighbours(self, coord):
        return self._neighbours(coord, 1)

    def lines(self, coord):
        for i in range(self.size):
            yield from self._neighbours(coord, i)

    def copy(self):
        pass


class RectMap(Map):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.height = len(data)
        self.width = len(max(data, key=len))
        self.size = max(self.height, self.width)

    def copy(self):
        return copy.deepcopy(self)

    def _neighbours(self, coord, i):
        if coord[1] < self.width-i:
            yield coord[0], coord[1]+i
        if coord[1] > 0:
            yield coord[0], coord[1]-i
        if coord[0] < self.height-i:
            yield coord[0]+i, coord[1]
        if coord[0] > 0:
            yield coord[0]-i, coord[1]

    def __iter__(self):
        for row in range(self.height):
            for col in range(self.width):
                yield row, col

    def __getitem__(self, coord):
        return self.data[coord[0]][coord[1]]

class HexMap(Map):
    def copy(self):
        return copy.deepcopy(self)

    def _neighbours(self, coord, i):
        x, y = coord
        if (x+i, y) in self:
            yield (x+i, y)
        if (x, y+i) in self:
            yield (x, y+i)
        if (x-i, y) in self:
            yield (x-i, y)
        if (x, y-i) in self:
            yield (x, y-i)
        if (x+i, y-i) in self:
            yield (x+i, y-i)
        if (x-i, y+i) in self:
            yield (x-i, y+i)


class TriMap(Map):
    pass


class Cell:
    def __init__(self, number, color = None) -> None:
        self.number = number
        self.color = color