import re
from structures import *


class Coder:
    def decode_cell(self, data: str) -> Cell:
        if re.match(r".\d", data):
            c = data[0]
            n = int(data[1])
            if c == "-":
                return Cell(n, 1)
            elif c == "#":
                return Cell(n, 0)
            else:
                return Cell(n)

    def encode_cell(self, cell: Cell) -> str:
        return f"{'-' if cell.color == 1 else '#' if cell.color == 0 else '.'}{cell.number}"


class RectCoder(Coder):
    def decode_map(self, data: str) -> RectMap:
        if re.match(r"((.\d )*.\d\n)*(.\d )*.\d", data):
            lines = data.split("\n")
            m = [line.split(" ") for line in lines]
            return RectMap([[item for item in map(self.decode_cell, line)] for line in m])

    def encode_map(self, m: Map) -> str:
        return "\n".join(" ".join(map(self.encode_cell, line)) for line in m.data)


class HexCoder(Coder):
    def decode_map(self, data: str) -> HexMap:
        lines = data.split("\n")
        data = {}
        row = 0
        for line in lines:
            m = line.split(' ')
            for col in range(len(m)):
                data[row, col] = self.decode_cell(m[col])
            row += 1
        result = HexMap(data)
        result.size = len(lines)
        return result

    def encode_map(self, m: Map) -> str:
        lines = {}
        for i,j in sorted(m):
            if i not in lines:
                lines[i] = f"{self.encode_cell(m[i, j])}"
            else:
                lines[i] += f" {self.encode_cell(m[i, j])}"
        return "\n".join(lines.values())