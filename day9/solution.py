def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return lines[0]


file_name = "test.txt"
data = read_input(file_name)


def map_input(inp: str):
    lengths = [int(char) for i, char in enumerate(inp) if i % 2 == 0]
    spaces = [int(char) for i, char in enumerate(inp) if i % 2 != 0]

    res = []
    l, s = 0, 0
    while l < len(lengths):
        for i in range(lengths[l]):
            res.append(str(l))
        if s < len(spaces):
            for i in range(spaces[s]):
                res.append('.')
            s += 1
        l += 1
    return res


def part1_solution():
    mapped = map_input(data)
    # print(mapped)

    left = 0
    right = len(mapped)-1
    while left < right:
        while left < len(mapped) and mapped[left] != '.':
            left += 1
        while right >= 0 and mapped[right] == '.':
            right -= 1
        if left < len(mapped) and right >= 0 and left < right:
            mapped[left], mapped[right] = mapped[right], mapped[left]

    print(mapped)
    sol = 0
    for i, char in enumerate(mapped):
        if char == ".":
            break
        sol += (i * int(char))
    print(sol)


def part2_solution():
    mapped = map_input(data)
    print(mapped)

    swapped = True
    left = 0
    right = len(mapped)-1
    while swapped:
        while right >= 0 and mapped[right] == '.':
            right -= 1
        num_to_swap = mapped[right]
        len_num = 0
        while right >= 0 and mapped[right] == num_to_swap:
            right -= 1
            len_num += 1

        while left < right and mapped[left] != ".":
            left += 1
        len_dot = 0
        while left < right and mapped[left] == ".":
            left += 1
            len_dot += 1

        if left < right and len_num <= len_dot:


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
