from dataclasses import dataclass


@dataclass
class Problem:
    operator: str
    nums: list[int]


def parse_input(include_spaces: bool = True):
    rows = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            # print(line)
            row = line
            if include_spaces:
                row = line.split(" ")
            rows.append(list(row))
    return rows


def build_grid(rows: list[list[str]]) -> list[list[str]]:
    grid = []

    for row in rows:
        grid.append([x for x in row if x])

    return grid


def part_one(rows: list[list[str]]) -> int:
    grid = build_grid(rows)

    for row in grid:
        print(row)
    print()
    x_len = len(grid)
    y_len = len(grid[0])

    problems: list[Problem] = []
    for y in range(y_len):
        operator = ""
        nums: list[int] = []
        for x in range(x_len):
            if x == x_len - 1:
                operator = grid[x][y]
            else:
                nums.append(int(grid[x][y]))
            # print(f"x: {x}, y: {y} \t {grid[x][y]}")
        problems.append(Problem(operator, nums))

    count = 0
    for problem in problems:
        answer = 0
        print(f"Current Problem: {problem}")
        if problem.operator == "*":
            answer = 1
            print()
            for num in problem.nums:
                print(f"ans: {answer}, num: {num}")
                answer = answer * num
        else:
            answer = sum(problem.nums)
        # print()
        # print(f"answer: {answer}")
        count += answer

    return count


def part_two(grid):
    max_y_length = max([len(row) for row in grid])

    # pad each row
    for row in grid:
        row += [" "] * (max_y_length - len(row))

    for row in grid:
        print(row)
    print()

    operations = []
    op_row = len(grid) - 1
    for i in range(max_y_length):
        char = grid[op_row][i]
        if char != " ":
            operations.append(char)

    problems = []

    problem = []
    for y in range(max_y_length):
        num = ""
        for x in range(len(grid)):
            char = grid[x][y]
            if x == op_row:
                continue
            num += char
            # print(grid[x][y], end="")
        num = num.replace(" ", "")
        if num:
            problem.append(int(num))
            # print(f"num: {num}")
        else:
            print()
            problems.append(problem)
            problem = []
    problems.append(problem)

    answers = []
    for i in range(len(problems)):
        op = operations[i]
        ans = 0
        if op == "*":
            ans = 1
            for num in problems[i]:
                ans = ans * num
        else:
            ans = sum(problems[i])
        answers.append(ans)
    print(problems)
    print(operations)
    print(answers)

    return sum(answers)


def main():
    rows = parse_input(False)
    # part_one_answer = part_one(rows)
    # print()
    # print(f"part 1: {part_one_answer}")
    part_two_answer = part_two(rows)
    print()
    print(f"part 2: {part_two_answer}")


main()
