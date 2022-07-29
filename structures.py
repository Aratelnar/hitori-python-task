import functools

class Map:
    def __init__(self, height = 0, width = 0, data = None) -> None:
        if data != None:
            self.extract_map(data)
        else:
            self.data = [[Cell(0)] * width] * height

    def __str__(self) -> str:
        return "\n".join(" ".join(map(str, line)) for line in self.data)

    def extract_map(self, data: str):
        lines = data.split("\n")
        m = [line.split(" ") for line in lines]
        self.data = [[item for item in map(Cell.extract_cell, line)] for line in m]


class Cell:
    def __init__(self, number, color = None) -> None:
        self.number = number
        self.color = color

    def __str__(self) -> str:
        return f"{'-' if self.color == 1 else '#' if self.color == 0 else '.'}{self.number}"

    def extract_cell(data: str):
        c = data[0]
        n = int(data[1])
        if c == "-":
            return Cell(n, 1)
        elif c == "#":
            return Cell(n, 0)
        else:
            return Cell(n)

with open("tests/8x8.txt", 'r') as f:
    print(Map(data=f.read()))