class CountSquares:

    def __init__(self):
        self.ptsCount = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        for (x, y), count in self.ptsCount.items():
            if abs(qx - x) == abs(qy - y) and qx != x and qy != y:
                res += count * self.ptsCount[(qx, y)] * self.ptsCount[(x, qy)]
        return res