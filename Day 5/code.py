from map import Map

def main():
    with open("./Day 5/input.txt") as f:
        input = f.readlines()
    one(input)


def one(input):
    map = Map(input)
    print(map)
    print(f"This map has {map.sumDangerPoints()} danger points")

if __name__ == "__main__":
    main()