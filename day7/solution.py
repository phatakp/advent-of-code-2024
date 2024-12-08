from functools import reduce
import operator


def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: x.replace("\n", "").split(': '), lines))


def add_and_mult(iterable: list[str]):
    return reduce()


def part1_solution():
    file_name = "test.txt"
    data = read_input(file_name)
    ans = 0
    for [res, nums_str] in data[::-1]:

        nums = nums_str.split(' ')
        sol = [int(nums[0])]
        for i, num in enumerate(nums):
            if i > 0:
                tmp = []
                for item in sol:
                    tmp.append(item*int(num))
                    tmp.append(item+int(num))
                sol = tmp.copy()
        if int(res) in sol:
            ans += int(res)
    print(ans)


def part2_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    ans = 0
    for [res, nums_str] in data[::-1]:

        nums = nums_str.split(' ')
        sol = [nums[0]]
        for i, num in enumerate(nums):
            if i > 0:
                tmp = []
                for item in sol:
                    tmp.append(item+num)
                    tmp.append(str(int(item)*int(num)))
                    tmp.append(str(int(item)+int(num)))
                sol = tmp.copy()
        if res in sol:
            ans += int(res)
    print(ans)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
