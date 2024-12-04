

def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        return list(map(lambda x: x.replace("\n", ""), lines))


def format_data(lines: list[str]):
    res = [line.split(" ") for line in lines]
    return list(map(lambda x: [int(y) for y in x], res))


def is_safe(line: list[int]):
    prev = 0
    diff = 0
    for i, num in enumerate(line):
        if (i == 0):
            prev = num
        elif (i == 1):
            diff = num-prev
            prev = num
            if abs(diff) not in (1, 2, 3):
                return False
        else:
            if abs(diff) not in (1, 2, 3):
                return False
            elif diff < 0 and num >= prev:
                return False
            elif diff > 0 and num <= prev:
                return False
            elif abs(num-prev) not in (1, 2, 3):
                return False
            else:
                diff = num-prev
                prev = num

    return True


def part1_solution():
    lines = read_input()
    data = format_data(lines)
    ans = sum([is_safe(line) for line in data])
    print(ans)


def part2_solution():
    lines = read_input()
    data = format_data(lines)
    ans = 0
    for line in data:
        if is_safe(line):
            ans += 1
        else:
            for i in range(len(line)):
                copy_data = line.copy()
                copy_data.pop(i)
                if is_safe(copy_data):
                    ans += 1
                    break
    print(ans)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
