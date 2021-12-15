def main():
    with open("./Day 8/input.txt") as f:
        lines = f.read().splitlines()

    print(f"Part one: number of unique-segment digits: {one(lines)}")
    two(lines)

def one(inputList):
    tally = 0
    
    secondHalf = [half.split(" | ")[1] for half in inputList]

    for half in secondHalf:
        for digit in half.split(" "):
            numLen = len(digit)
            # print(f"digit {digit} is numLen {numLen}")
            if numLen == 2 or numLen == 4 or numLen == 3 or numLen == 7: 
                tally += 1
                # print(digit)
    return tally

def two(inputList):
    sum = 0
    for line in inputList:
    # if True:
        unknownSignals = sorted(line.split(" | ")[0].split(" "), key=len)
        outputList = line.split(" | ")[1].split(" ")

        # numbers = [0 for i in range(10)]
        numbers = {1: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        segments = {'top': '', 'topLeft': '', 'topRight': '', 'center': '', 'bottomLeft': '', 'bottomRight': '', 'bottom': ''}

        # deal with the unique numbers first
        if True:
            unknownSignalsEditable = unknownSignals.copy()
            for signal in unknownSignals:
                # print(f"doing {signal} within set {unknownSignalsEditable}")
                if len(signal) == 2:
                    numbers.update({1: "".join(sorted(signal))})
                    unknownSignalsEditable.remove(signal)

                if len(signal) == 3:
                    numbers.update({7: "".join(sorted(signal))})
                    unknownSignalsEditable.remove(signal)

                if len(signal) == 4:
                    numbers.update({4: "".join(sorted(signal))})
                    unknownSignalsEditable.remove(signal)

                if(len(signal)) == 7:
                    numbers.update({8: "".join(sorted(signal))})
                    unknownSignalsEditable.remove(signal)
            unknownSignals = unknownSignalsEditable
        # determine what is the top segment: the segment that is in 7 but not in 1
        # print(f"\t 7: {numbers.get(7)}")
        segments.update({'top': [seg for seg in numbers.get(7) if seg not in set(numbers.get(1))][0]})

        # --- deal with signals with length 5 ---
        # possibilities: 2, 3, 5

        # find number 3: unknown signal of length 5 that contains both segments from 1
        # print([sig for sig in unknownSignals if len(sig) == 5 and set(numbers.get(1)).issubset(set(sig))][0])
        threeSignal = [sig for sig in unknownSignals if len(sig) == 5 and set(numbers.get(1)).issubset(set(sig))][0]
        numbers.update({3: "".join(sorted(threeSignal))})
        unknownSignals.remove(threeSignal)

        # based on that:
        # find the center segment: the one that is -is in both 3 and 4 AND -is not in 1
        segments.update({'center': [seg for seg in threeSignal if seg in set(numbers.get(4)) and seg not in set(numbers.get(1))][0]})
        # find the bottom segment: the one that is -in three but not in 4 AND -not the top one (AKA not in 7)
        segments.update({'bottom': [seg for seg in threeSignal if seg not in set(numbers.get(4)) and seg not in set(numbers.get(7))][0]})
        # find the top left segment: the one that is in 4 but not 3
        segments.update({'topLeft': [seg for seg in numbers.get(4) if seg not in set(numbers.get(3))][0]})

        # find number 5  (2 or 5 left): unknown signal of length 5 that contains top left segment
        fiveSignal = [sig for sig in unknownSignals if len(sig) == 5 and segments.get('topLeft') in set(sig)][0]
        numbers.update({5: "".join(sorted(fiveSignal))})
        unknownSignals.remove(fiveSignal)

        # based on that:
        # find the bottom right segment: the only unknown segment in 5
        segments.update({'bottomRight': [seg for seg in list(numbers.get(5)) if seg not in set(segments.values())][0]})

        # find number 2: leftover
        twoSignal = [sig for sig in unknownSignals if len(sig) == 5][0]
        numbers.update({2: "".join(sorted(twoSignal))})
        unknownSignals.remove(twoSignal)

        # based on that:
        # find the bottom left segment: the segment in 2 that is not top righht
        segments.update({'bottomLeft': [seg for seg in list(numbers.get(2)) if (seg not in (segments.values()) and seg not in set(numbers.get(1)))][0]})

        # finally: 
        # the last segment, top right, is the last unknown segment 
        segments.update({'topRight': [seg for seg in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if seg not in set(segments.values())][0]})
        
        # left: 0, 6, 9
        for signal in unknownSignals:
            if segments.get('center') not in set(signal):
                numbers.update({0: "".join(sorted(signal))})
                continue
                
            if segments.get('bottomLeft') not in set(signal):
                numbers.update({9: "".join(sorted(signal))})
                continue

            if segments.get('topRight') not in set(signal):
                numbers.update({6: "".join(sorted(signal))})


        # print(f"Gone through line {line}!\n{segments}\n{numbers}")

        number = ""

        for digit in outputList:
            number += (str(list(numbers.keys())[list(numbers.values()).index("".join(sorted(digit)))]))

        print(f"found output number {outputList}:{number}")
        sum += int(number)

    print(f"final number is! {sum}")



if __name__ == "__main__":
    main()