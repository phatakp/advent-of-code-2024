from collections import Counter


def read_input():
    nums1 = []
    nums2 = []
    with open("test.txt") as f:
        lines = f.readlines()
        return list(map(lambda x: x.replace("\n", ""), lines))


def format_data(lines: list[str]):
    res = [line.split("   ") for line in lines]
    return (list(map(lambda x: int(x[0]), res)), list(map(lambda x: int(x[1]), res)))


def part1_solution():
    lines = read_input()
    (nums_list1, nums_list2) = format_data(lines)
    nums_list1.sort()
    nums_list2.sort()
    sum = 0
    for (i, num) in enumerate(nums_list1):
        sum += abs(nums_list2[i]-num)

    print(sum)


def part2_solution():
    lines = read_input()
    (nums_list1, nums_list2) = format_data(lines)
    res = Counter(nums_list2)
    sum = 0
    for (i, num) in enumerate(nums_list1):
        sum += num * res[num]

    print(sum)


def main():
    part1_solution()
    # part2_solution()


if __name__ == "__main__":
    main()
