def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return list(map(lambda x: list(x.replace("\n", "")), lines))


data = read_input('input.txt')
directions = {'N': (-1, 0), 'E': (0, 1), "W": (0, -1), "S": (1, 0)}
turn_right = {'N': 'E', 'E': 'S', "W": 'N', "S": 'W'}


def part1_solution():
    curr_direction = 'N'
    [(row, col),] = [(row, col) for row in range(len(data))
                     for col in range(len(data[0])) if data[row][col] == "^"]
    visited = {(row, col)}

    while 0 <= row < len(data) and 0 <= col < len(data[0]):
        if (curr_direction == 'N' and row == 0) or (curr_direction == 'E' and col == len(data[0])-1) or (curr_direction == 'S' and row == len(data)-1) or (curr_direction == 'W' and col == 0):
            visited.add((row, col))
            break

        nr, nc = directions[curr_direction]
        if data[row+nr][col+nc] != '#':
            row += nr
            col += nc
            visited.add((row, col))
        else:
            curr_direction = turn_right[curr_direction]

    print(len(visited))
    return visited


def part2_solution():
    [(init_row, init_col),] = [(row, col) for row in range(len(data))
                               for col in range(len(data[0])) if data[row][col] == "^"]
    visited = part1_solution()

    sol = 0
    for (r, c) in visited:
        curr_direction = 'N'
        data_copy = [row[:] for row in data]
        if (data_copy[r][c] != '^'):
            data_copy[r][c] = '#'
            row, col = init_row, init_col
            try_visited = {(row, col, curr_direction)}

            while 0 <= row < len(data_copy) and 0 <= col < len(data_copy[0]):
                if (curr_direction == 'N' and row == 0) or (curr_direction == 'E' and col == len(data[0])-1) or (curr_direction == 'S' and row == len(data)-1) or (curr_direction == 'W' and col == 0):
                    try_visited.add((row, col, curr_direction))
                    break

                nr, nc = directions[curr_direction]
                if data_copy[row+nr][col+nc] != '#':
                    row += nr
                    col += nc
                    try_visited.add((row, col, curr_direction))
                else:
                    curr_direction = turn_right[curr_direction]
                    if (row, col, curr_direction) in try_visited:
                        sol += 1
                        break
                    else:
                        try_visited.add((row, col, curr_direction))

    print(sol)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
