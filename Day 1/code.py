def main():
    with open("./inputs/DayOne.txt") as f:
        nums = [int(line) for line in f.readlines()]
    one(nums)
    two(nums)

def one(nums):
    increased = 0

    for i in range(1, len(nums)):
        if (nums[i-1] < nums[i]): increased += 1


    print(f"Part one: {increased}")


def two(nums):
    increased = 0

    for i in range(3, len(nums)):
        prevSum = sum(nums[i-3:i])
        newSum = sum(nums[i-2:i+1])
        if (prevSum < newSum): increased += 1

    print (f"Part two: {increased}")


if __name__ == "__main__":
    main()