import string
lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
digits = [str(x) for x in list(range(10))]
file_name = "input.txt"


def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: list(x.replace("\n", "")), lines))


data = read_input(file_name)


def get_distance(pos1: tuple[int, int], pos2: tuple[int, int]):
    return pos2[0]-pos1[0], pos2[1]-pos1[1]


def find_pos(char: str):
    return [(row, col) for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == char]


def part1_solution():
    antinodes = set()
    visited = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char in lowers or char in uppers or char in digits:
                char_pos = find_pos(char)
                visited.add((row, col))
                for (r, c) in char_pos:
                    if (r, c) not in visited:
                        (row_diff, col_diff) = get_distance((row, col), (r, c))
                        if (col <= c):
                            left_row = row-row_diff
                            left_col = col-col_diff
                            right_row = r+row_diff
                            right_col = c+col_diff
                        else:
                            left_row = r+row_diff
                            left_col = c+col_diff
                            right_row = row-row_diff
                            right_col = col-col_diff

                        if 0 <= left_row < len(data) and 0 <= left_col < len(data[0]):
                            if data[left_row][left_col] != char:
                                antinodes.add((left_row, left_col))
                        if 0 <= right_row < len(data) and 0 <= right_col < len(data[0]):
                            if data[right_row][right_col] != char:
                                antinodes.add((right_row, right_col))

    print(len(antinodes))


def part2_solution():
    antinodes = set()
    visited = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char in lowers or char in uppers or char in digits:
                char_pos = find_pos(char)
                visited.add((row, col))
                for (r, c) in char_pos:
                    if (r, c) not in visited:
                        (row_diff, col_diff) = get_distance((row, col), (r, c))
                        if (col <= c):
                            left_row = row-row_diff
                            left_col = col-col_diff
                            right_row = r+row_diff
                            right_col = c+col_diff
                        else:
                            left_row = r+row_diff
                            left_col = c+col_diff
                            right_row = row-row_diff
                            right_col = col-col_diff

                        r1, c1 = left_row, left_col
                        r2, c2 = right_row, right_col
                        while 0 <= r1 < len(data) and 0 <= c1 < len(data[0]):
                            if data[r1][c1] != char:
                                antinodes.add((r1, c1))
                            if r1 <= r2:
                                r1 -= (row_diff if row_diff >
                                       0 else row_diff*-1)
                                c1 -= (col_diff if col_diff >
                                       0 else col_diff*-1)
                            else:
                                r1 += (row_diff if row_diff >
                                       0 else row_diff*-1)
                                c1 -= (col_diff if col_diff >
                                       0 else col_diff*-1)
                                left_row += row_diff
                                left_col -= col_diff
                        r1, c1 = left_row, left_col
                        while 0 <= r2 < len(data) and 0 <= c2 < len(data[0]):
                            if data[r2][c2] != char:
                                antinodes.add((r2, c2))
                            if r1 <= r2:
                                r2 += (row_diff if row_diff >
                                       0 else row_diff*-1)
                                c2 += (col_diff if col_diff >
                                       0 else col_diff*-1)
                            else:
                                r2 -= (row_diff if row_diff >
                                       0 else row_diff*-1)
                                c2 += (col_diff if col_diff >
                                       0 else col_diff*-1)
    print(len(antinodes.union(visited)))
    # for r, line in enumerate(data):
    #     print()
    #     for c, char in enumerate(line):
    #         print(char if (r, c) not in antinodes else '#', end=" ")


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
