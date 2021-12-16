def main():
    with open("./Day 9/input.txt") as f:
        input = f.read().splitlines()

    map = Map(input)
    print(f"Part one: {map.addLowPonints()}")
    
    # part two
    map.findBasins()
    print(f"Part two: {map.findPartTwo()}")
    


class Map:
    def __init__(self, inputList):
        self.map = [[int(i) for i in row] for row in inputList]
        self.basins = []

    def addLowPonints(self):
        sum = 0
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.isLowPoint(row, col): sum += self.map[row][col] + 1
        return sum
    
    def isLowPoint(self, row, col):
        if row < 0 or row >= len(self.map) or col < 0 or col >= len(self.map[0]): return True
        point = self.map[row][col]
        return (
            self.isLowerThan(row, col, row-1, col)
            and self.isLowerThan(row, col, row+1, col)
            and self.isLowerThan(row, col, row, col-1)
            and self.isLowerThan(row, col, row, col+1)
        )

    def isLowerThan(self, r1, c1, r2, c2):
        if self.isOutOfRange(r2, c2): return True
        return self.map[r1][c1] < self.map[r2][c2]

    def isOutOfRange(self, r, c):
        return r < 0 or r >= len(self.map) or c < 0 or c >= len(self.map[r])

    def findBasins(self):
        mapped = [[False for b in range(len(self.map[row]))] for row in range(len(self.map))]
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if not mapped[row][col]:
                    self.basins.append(self.findBasin(mapped, row, col))

        # print(self.basins)

    def findBasin(self, alreadyMapped, row, col):
        basin = []
        # print(f"finding basin at loc {col},{row}")
        if self.isOutOfRange(row, col):
            # print(f"\tnope, out of range")
            return basin
        if self.map[row][col] == 9 or alreadyMapped[row][col]:
            # print(f"\tnope, 9 ({self.map[row][col] == 9}) or already mapped ({alreadyMapped[row][col] })")
            return basin
        # print(f"\tdigging!")
        basin.append((row,col))
        alreadyMapped[row][col] = True
        basin.extend(self.findBasin(alreadyMapped, row+1, col))
        basin.extend(self.findBasin(alreadyMapped, row-1, col))
        basin.extend(self.findBasin(alreadyMapped, row, col+1))
        basin.extend(self.findBasin(alreadyMapped, row, col-1))
        return basin

    def findPartTwo(self):
        prod = 1
        sortedBasins = sorted(self.basins, key=len)
        print(sortedBasins)
        for basin in reversed(range(len(self.basins)-3, len(self.basins))):
            if basin == []: pass
            prod *= len(sortedBasins[basin])
            print(f"prod: {prod} * {len(sortedBasins[basin])}")
        return prod



if __name__ == "__main__":
    main()