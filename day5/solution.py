def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: x.replace("\n", ""), lines))


def part1_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    orders = [item.split("|") for item in data if "|" in item]
    inp = [item.split(',') for item in data if "," in item]

    order_dict = dict()
    for a, b in orders:
        order_dict.setdefault(a, []).append(b)

    sol = 0
    for item in inp:
        valid = True
        for i in range(len(item)-1):
            for j in range(i+1, len(item)):
                if item[j] in order_dict and item[i] in order_dict[item[j]]:
                    valid = False
                    break
            if not valid:
                break
        if (valid):
            sol += int(item[len(item)//2])
    print(sol)


def part2_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    orders = [item.split("|") for item in data if "|" in item]
    inp = [item.split(',') for item in data if "," in item]

    order_dict = dict()
    for a, b in orders:
        order_dict.setdefault(a, []).append(b)

    sol = 0
    for item in inp:
        changed = False
        for i in range(len(item)-1):
            for j in range(i+1, len(item)):
                if item[j] in order_dict and item[i] in order_dict[item[j]]:
                    changed = True
                    item[i], item[j] = item[j], item[i]
        if (changed):
            sol += int(item[len(item)//2])
    print(sol)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
