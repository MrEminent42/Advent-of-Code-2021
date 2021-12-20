with open("./Day 11/input.txt") as f:
    lines = f.read().splitlines()

grid = [[int(i) for i in line] for line in lines]
flashCount = [0]

STEPS = 300

def printGrid():
    for line in grid:
        s = ""
        for i in line:
            if i == 0:
                s += "\033[1m" + str(i) + "\033[0m"
            else: s += str(i)
        print(s)

def nearbyEnergy(row, col):
    if not (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])):
        if not grid[row][col] == 0: 
            grid[row][col] += 1
            checkFlash(row,col)


def checkFlash(row, col):
    # check validity of position
    if row >= len(grid) or row < 0 or col >= len(grid) or col < 0: return
   
    # check if location needs to be flashed
    if grid[row][col] < 10: return
    
    # print(f"flashing! r,c {row},{col} because of energy {grid[row][col]}")

    flashCount[0] += 1
    grid[row][col] = 0

    nearbyEnergy(row-1, col-1)
    nearbyEnergy(row-1, col)
    nearbyEnergy(row-1, col+1)
    
    nearbyEnergy(row, col-1)
    nearbyEnergy(row, col+1)
    
    nearbyEnergy(row+1, col-1)
    nearbyEnergy(row+1, col)
    nearbyEnergy(row+1, col+1)


for step in range(1, STEPS+1):
    startFlashCount = flashCount[0]

    for row in range(len(grid)):
        # print(f"starting row {row}")
        for col in range(len(grid[row])):
            # print(f"\tstarting col {col}")
            # increaseEnergy(row, col)
            grid[row][col] += 1

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            checkFlash(row,col)

    # print(f"in step {step}:")
    # if (step > 192): printGrid()
    print(f"flash count after step {step}: {flashCount[0]}")

    if startFlashCount + 100 == flashCount[0]:
        print(f"ALL FLASHED AT STEP {step}!")
