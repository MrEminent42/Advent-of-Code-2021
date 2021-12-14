def main():
    with open("./Day 2/inputs.txt") as f:
        inputs = f.readlines()

    commands = findCommands(inputs)

    one(commands)
    two(commands)

    

def one(commands):
    x = 0
    y = 0

    for command in commands:
        if (command[0] == 0): x += command[1]
        if (command[0] == 1): y -= command[1]
        if (command[0] == 2): y += command[1]

    print(f"ONE: X: {x}, Y: {y}, X*Y: {x*y}")

def two(commands):
    x = 0
    y = 0
    aim = 0

    for command in commands:
        if (command[0] == 0): 
            x += command[1]
            y += aim*command[1]
        if (command[0] == 1): 
            aim -= command[1]
        if (command[0] == 2): 
            aim += command[1]

    print(f"TWO: X: {x}, Y: {y}, X*Y: {x*y}")

def parseDir(string):
    type = {
        "forward": 0,
        "up": 1,
        "down": 2
    }
    return type.get(string)

def findCommands(inputs):
    # DIRECTIONS: forward=0; up=1; down=2; 
    commands = []

    for i in inputs:
        line = str.split(i, " ")
        commands.append((parseDir(line[0]), int(line[1])))

    return commands

if __name__ == "__main__":
    main()