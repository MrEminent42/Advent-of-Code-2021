with open("./Day 10/input.txt") as f:
    lines = f.read().splitlines()

closers = {'(':')', '<':'>', '{':'}', '[':']'}
syntaxError = {')':3, ']':57, '}':1197, '>':25137}
autoCompleteScore = {')':1, ']':2, '}':3, '>':4}


error = 0
scores = []

for line in lines:
    order = []
    corrupt = False
    # print(f"looking at line {line}")

    for char in line:
        # if the character is an opening character
        if char in closers.keys():
            # add it to the order list
            order.append(char)
            # print(f"\t appended char {char}")
        elif char in closers.values():
            # print(f"\t looking at closer {char}")
            # if this character matches the most recently opened chunk
            mostRecentlyOpenedChunk = order.pop()
            matches = char == closers.get(mostRecentlyOpenedChunk)
            # print(f"\t\tmatches: {matches}")
            if not matches:
                error += syntaxError.get(char)
                corrupt = True
                # print(f"line {line} had syntax error {syntaxError.get(char)} because of char {char}")
                break

    if corrupt: continue

    lineScore = 0
    # while there are still open chunks (and the line isn't corrupt)
    while len(order) > 0:
        lineScore *= 5
        lineScore += autoCompleteScore.get(closers.get(order.pop()))
    
    scores.append(lineScore)


scores.sort()

print(f"Part one total error: {error}")
print(f"Part two score: {scores[int(len(scores)/2)]}")
print(f"\t{scores}")
