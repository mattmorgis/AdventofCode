def parse_input() -> list[str]:
    grid: list[str] = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            grid.append(line)
    return grid


def check_neighbors(grid: list[str], x: int, y: int) -> bool:
    print(f"checking neighbors for coord: {x}, {y}")
    end_row = len(grid)
    end_column = len(grid[x])
    print(f"end of right grid: {end_column}, bottom: {end_row}")

    neighbors_with_rolls = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            print(f"neighbor: {i}, {j}", end="\t")
            if i >= 0 and i < end_column and j >= 0 and j < end_column:
                if i == x and j == y:
                    print("target")
                else:
                    if grid[i][j] == "@":
                        neighbors_with_rolls += 1
                        print("hit")
                    else:
                        print("miss")
            else:
                print("invalid, skipped")

    print(f"neighbors_with_rolls: {neighbors_with_rolls}")
    return neighbors_with_rolls < 4


def part_one(grid: list[str]) -> int:
    repeat = True
    acc = 0

    while repeat:
        coords = []
        print()
        print("new batch")
        can_move = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                # print(f"x: {x}, y: {y}")
                char = grid[x][y]
                # print(char, end="")

                if char == "@":
                    hit = check_neighbors(grid, x, y)
                    if hit:
                        can_move += 1
                        coords.append((x, y))
                        print(f"HIT! {x}, {y}")
        acc += can_move

        if can_move == 0:
            repeat = False
        else:
            for i, j in coords:
                chars = list(grid[i])
                chars[j] = "x"
                grid[i] = "".join(chars)

    return acc


def main():
    grid = parse_input()
    part_one_answer = part_one(grid)
    print()
    print(f"part 1: {part_one_answer}")


main()
