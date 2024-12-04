import re


def read_input(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
        return "".join(list(map(lambda x: x.replace("\n", ""), lines)))


def part1_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    pattern = re.compile(r"mul[(]([\d]{1,3},[\d]{1,3})[)]")
    nums = pattern.findall(data)
    ans = 0
    for num in nums:
        a, b = num.split(',')
        ans += (int(a) * int(b))
    print(ans)


def part2_solution():
    file_name = "input.txt"
    data = read_input(file_name)
    pattern = re.compile(r"mul[(]([\d]{1,3},[\d]{1,3})[)]")
    pattern_do = re.compile(r"do[(][)]")
    pattern_dont = re.compile(r"don't[(][)]")
    nums = pattern.findall(data)
    numpos = [match.start()
              for match in re.finditer(pattern, data)]
    dos = [match.start()
           for match in re.finditer(pattern_do, data)]
    donts = [match.start()
             for match in re.finditer(pattern_dont, data)]

    ans = 0
    for i, num in enumerate(nums):
        include = False
        a, b = num.split(',')
        n = 0
        d = 0
        while n < len(donts) and donts[n] < numpos[i]:
            n += 1
        if n > 0:
            n -= 1
        dont = donts[n]

        while d < len(dos) and dos[d] < numpos[i]:
            d += 1
        if d > 0:
            d -= 1
        do = dos[d]

        if dont > numpos[i] or dont < do < numpos[i]:
            include = True

        if include:
            ans += (int(a) * int(b))
        else:
            print(num, 'at', numpos[i])
    print(ans)


def main():
    # part1_solution()
    part2_solution()


if __name__ == "__main__":
    main()
