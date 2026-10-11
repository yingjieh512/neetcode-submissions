class CountSquares:

    def __init__(self):
        self.cols = {}

    def add(self, point: List[int]) -> None:
        x, y = point

        if x not in self.cols:
            self.cols[x] = {}

        if y not in self.cols[x]:
            self.cols[x][y] = 0

        self.cols[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        if x not in self.cols:
            return 0

        for y2, count in self.cols[x].items():
            if y2 == y:
                continue

            d = y2 - y

            for nx in [x + d, x - d]:
                if nx in self.cols:
                    result += (count *
                               self.cols[nx].get(y, 0) *
                               self.cols[nx].get(y2, 0))

        return result