def main():

    with open("./Day 3/input.txt") as f:
        inputs = f.readlines()

    ones = one(inputs)
    print(f"Gamma: {ones[0]} aka {int(ones[0], 2)}, epsilon: {ones[1]} aka {int(ones[1], 2)}")
    print(f"Gamma * epsilon = {int(ones[0], 2)*int(ones[1], 2)}")

    twos = two(inputs)
    print(f"Oxygen Generator Rating: {int(twos[0][0])} aka {int(twos[0][0], 2)}, CO2 Scrubber Rating {int(twos[1][0])} aka {int(twos[1][0], 2)}")
    print(f"Oxygen * CO2 = {int(twos[0][0], 2)*int(twos[1][0], 2)}")


def one(input):
    gamma = ""
    epsilon = ""
    # for each column/digit
    for digit in range(len(input[0]) - 1):
        # # print(f"analyzing digit {digit}")
        # zeroes = 0
        # ones = 1
        # # run through each row
        # for val in input:
        #     if int(val[digit]) == 0: zeroes += 1
        #     if int(val[digit]) == 1: ones += 1

        vals = mostCommonAndLeastCommonDigits(input, digit)

        gamma += vals[0]
        epsilon += vals[1]

        # print(f"Gamma: {gamma} aka {int(gamma, 2)}, epsilon: {epsilon} aka {int(epsilon, 2)}")
    return (gamma, epsilon)

def two(inputs):
    vals = (oxygenGeneratorRating(inputs, 0), CO2ScrubberRating(inputs, 0))
    return vals

def oxygenGeneratorRating(inputs, digit):
    # print(inputs)
    if (len(inputs) < 2): return inputs

    vals = mostCommonAndLeastCommonDigits(inputs, digit)
    newInputs = []
    for input in inputs: 
        if vals != -1: 
            if input[digit] == vals[0]: newInputs.append(input)
            continue
        # keep values with 1 if 1s and 0s are equally common
        if input[digit] == "1": newInputs.append(input)

    # print(newInputs)
    return (oxygenGeneratorRating(newInputs, digit+1))

def CO2ScrubberRating(inputs, digit):
    # print(inputs)
    if (len(inputs) < 2): return inputs

    vals = mostCommonAndLeastCommonDigits(inputs, digit)
    newInputs = []
    for input in inputs: 
        if vals != -1: 
            if input[digit] == vals[1]: newInputs.append(input)
            continue
        # keep values with 0 if 1s and 0s are equally common
        if input[digit] == "0": newInputs.append(input)

    # print(newInputs)
    return (CO2ScrubberRating(newInputs, digit+1))


def mostCommonAndLeastCommonDigits(inputs, digit):
    # for digit in range(len(input[0]) - 1):
        # print(f"analyzing digit {digit}")
    zeroes = 0
    ones = 0
    # run through each row
    for val in inputs:
        if int(val[digit]) == 0: 
            zeroes += 1
            continue
        if int(val[digit]) == 1: 
            ones += 1
    
    if (ones > zeroes): return ("1", "0")
    if (ones < zeroes): return ("0", "1")
    # print(f"Same! {zeroes} 0s and {ones} 1s in loc {digit}")
    return -1

    

if __name__ == "__main__":
    main()