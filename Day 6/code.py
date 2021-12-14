def main():
    with open("./Day 6/input.txt") as f:
        one(f.readlines(), 256)

def one(text, days):
    pop = Population(text[0].split(","))

    newPop = PopulationTwo(text[0].split(","))
    # for day in range(days):
        # pop.passDay()


class Population:
    def __init__(self, inputList):
        self.pop = [int(i) for i in inputList]
        self.days = 0
        print(f"At the beginning: {self.pop}")
    
    def passDay(self):
        self.days += 1
        startingLength = len(self.pop)
        for i in range(startingLength):
            self.pop[i] -= 1
            if self.pop[i] == -1:
                self.pop.append(8)
                self.pop[i] = 6
        print(f"At the end of day {self.days} there are {len(self.pop)} fish.")

class PopulationTwo:
    def __init__(self, inputList):
        self.fishCount = {i: 0 for i in range(0,8+1)}
        for fish in inputList:
            self.fishCount.update({int(fish): self.fishCount.get(int(fish)) + 1})
        # print(f"at the beginning: {sum(self.fishCount.values())} fish total")
        self.passDays(256)

    def passDays(self, numDays):
        for day in range(1, numDays+1):
            self.passDay()
            print(f"after day {day}, there are {sum(self.fishCount.values())} fish")

    def passDay(self):
        newFish = int(self.fishCount.get(0))
        # print(f"\t today there should be {newFish} new fish!")
        for age in range(0,8):
            self.fishCount.update({age: int(self.fishCount.get(age+1))})
        # print(f"\t today there should be {newFish} new fish!")
        self.fishCount.update({6: self.fishCount.get(6)+newFish})
        self.fishCount.update({8: newFish})
        print(f"\t{self.fishCount}")



if __name__ == "__main__":
    main()