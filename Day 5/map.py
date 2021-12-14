class Map:
    def __init__(self, inputLines):
        # self.map = [[0 for int in range(10)] for arr in range (10)]
        self.map = [[0 for int in range(992)] for arr in range (992)]
        for line in inputLines:
            parsedLine = self.parseLine(line)
            #if isStraightLine(parsedLine):
            self.addLine(parsedLine)
                # print(f"adding line {parsedLine}")


    def parseLine(self, line):
        start = str(line).split(" -> ")[0].split(",")
        fin = str(line).split(" -> ")[1].split("\n")[0].split(",")
        return [int(start[0]), int(start[1]), int(fin[0]), int(fin[1])]
        #returns (x1, y1, x2, y2)

    def addLine(self, line):
        if isStraightLine(line):
            # print(f"adding line {line} and going from x {line[0]} to {line[2]} and y {line[1]} to {line[3]}")
            for x in range(low(line[0], line[2]), high(line[0], line[2])+1):
                for y in range(low(line[1], line[3]), high(line[1], line[3])+1):
                    # print(f"row {x} and col {y} is now {self.map[y][x]+1}")
                    self.map[y][x] += 1
        else:
            xList = list(range(line[0], line[2]+1) if line[0] < line[2] else reversed(range(line[2], line[0]+1)))
            yList = list(range(line[1], line[3]+1) if line[1] < line[3] else reversed(range(line[3], line[1]+1)))

            # yRange = None
            # xRange = None

            # if x1 < x2: x1 to x2
            # if line[0] < line[2]:
            #     xRange = range(line[0], line[2]+1)
            #     # if y2 > y1:
            #     if line[line[1] > line[3]]: xRange

            # print(f"adding line {line} and going DIAGONALLY from x {xList[0]} to {xList[len(xList)-1]} and y {yList[0]} to {yList[len(yList)-1]}")
            for i in range(len(xList)):
                # print(f"doing point {xList[i]},{yList[i]}")
                self.map[yList[i]][xList[i]] += 1
                #print(f"row {y} and col {x} is now {self.map[x][y]+1}")

    def sumDangerPoints(self):
        sum = 0
        for row in self.map:
            for col in row:
                if col > 1: sum += 1

        return sum


    def __str__(self):
        # string = ""
        # for row in range(0,990):
        #     rowString: str = ""
        #     for col in range(0,990):
        #         if map[row][col] < 1: rowString = rowString + "."
        #         else: rowString += str(map[row][col])
        #     string = rowString + "\n"
        for line in self.map: print(line)
        return ""

    
def isStraightLine(line):
    return line[0] == line [2] or line [1] == line[3]

def low(one, two):
    if one > two: return two
    return one

def high(one, two):
    if (one > two): return one
    return two