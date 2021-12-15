def main():
    with open("./Day 7/input.txt") as f:
        pop = CrabPopulation(f.readlines()[0])
        loc = pop.findBestCost(0, len(pop.locations))
        newLoc = pop.findNewBestCost(0, len(pop.locations))
        print(f"Part one: the cheapest cost is at {loc} and is cost {pop.costToAlign(loc)}")
        
        print(f"Part two: the cheapest cost is at {newLoc} and is cost {pop.newCostToAlign(newLoc)}")




class CrabPopulation:
    def __init__(self, inputText):
        self.locations = [int(i) for i in inputText.split(",")]
        self.locations.sort()

    def findBestCost(self, start, end):
        print(f"Checking cost from {start} to {end}")
        if (start == end): return start
        halfway = start+int((end-start)/2)
        startCost = self.costToAlign(int(start))
        halfwayCost = self.costToAlign(int(start/end))
        endCost = self.costToAlign(int(end))
        
        if (end - start) < 3:
            minCost = min(startCost, halfwayCost, endCost)
            if (minCost == startCost):
                return start
            if (minCost == halfwayCost):
                return halfway
            if (minCost == endCost):
                return halfway
        print(f"\t cost to align start{start}/half{halfway}/end{end}: {startCost}, {halfwayCost}, {endCost}")

        if endCost < startCost:
            print(f"Lower cost found at {end}")
            return self.findBestCost(halfway, end)
        if startCost < endCost:
            print(f"Lower cost found at {start}")
            return self.findBestCost(start, halfway)
        
        print(f"Neither, doing 3/2")
        return self.findBestCost(start + halfway/2, end - halfway/2)

    def findNewBestCost(self, start, end):
        print(f"Checking NEW cost from {start} to {end}")
        if (start == end): return start
        halfway = start+int((end-start)/2)
        startCost = self.newCostToAlign(int(start))
        halfwayCost = self.newCostToAlign(int(start/end))
        endCost = self.newCostToAlign(int(end))
        
        if (end - start) < 3:
            minCost = min(startCost, halfwayCost, endCost)
            print(f"\t cost to align start{start}/half{halfway}/end{end}: {startCost}, {halfwayCost}, {endCost}")
            if (minCost == startCost):
                return start
            if (minCost == halfwayCost):
                return halfway
            if (minCost == endCost):
                print(f"returning end!")
                return end
        print(f"\t cost to align start{start}/half{halfway}/end{end}: {startCost}, {halfwayCost}, {endCost}")

        if endCost < startCost:
            print(f"Lower cost found at {end}")
            return self.findNewBestCost(halfway, end)
        if startCost < endCost:
            print(f"Lower cost found at {start}")
            return self.findNewBestCost(start, halfway)
        
        print(f"Neither, doing 3/2")
        return self.findNewBestCost(start + halfway/2, end - halfway/2)


    def costToAlign(self, loc):
        sum = 0
        for crab in self.locations:
            sum += abs(loc - crab)
        return sum
        
    def newCostToAlign(self, loc):
        sum = 0
        for crab in self.locations:
            distance = abs(loc - crab)
            sum += int((distance ** 2 + distance)/2)
        return sum



if __name__ == "__main__":
    main()