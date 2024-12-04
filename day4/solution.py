def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: list(x.replace("\n", "")), lines))


def part1_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    sol = 0

    # Row calculations
    for str_ in data:
        for i in range(len(str_)-3):
            if ''.join(str_[i:i+4]) in ('XMAS', 'SAMX'):
                sol += 1

    # Col calculations
    for str_ in zip(*data):
        for i in range(len(str_)-3):
            if ''.join(str_[i:i+4]) in ('XMAS', 'SAMX'):
                sol += 1

    # Diagonal calculations
    for row in range(len(data)-3):
        for col in range(len(data[0])-3):
            str_ = ""
            for i in range(4):
                str_ += data[row+i][col+i]
            if str_ in ('XMAS', 'SAMX'):
                sol += 1

    # Backward Diagonal calculations
    for row in range(len(data)-3):
        for col in range(len(data[0])-1, 2, -1):
            str_ = ""
            for i in range(4):
                str_ += data[row+i][col-i]
            if str_ in ('XMAS', 'SAMX'):
                sol += 1

    print(sol)


def part2_solution():
    file_name = "input.txt"
    data = read_input(file_name)

    sol = 0

    for row in range(1, len(data)-1):
        for col in range(1, len(data[0])-1):
            if data[row][col] == 'A':
                if data[row-1][col-1] in ('M', 'S') and data[row+1][col+1] in ('M', 'S') and data[row+1][col-1] in ('M', 'S') and data[row-1][col+1] in ('M', 'S'):
                    if data[row-1][col-1] != data[row+1][col+1] and data[row+1][col-1] != data[row-1][col+1]:
                        sol += 1

    print(sol)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
