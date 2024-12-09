def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: x.replace("\n", ""), lines))


def part1_solution():
    file_name = "test.txt"
    data = read_input(file_name)
    pass


def part2_solution():
    file_name = "test.txt"
    data = read_input(file_name)
    pass


def main():
    part1_solution()
    # part2_solution()


if __name__ == "__main__":
    main()
