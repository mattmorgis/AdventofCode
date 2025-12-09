def parse_input():
    rows = []
    with open("input-test.txt") as file:
        while line := file.readline().rstrip():
            rows.append(list(line))
    return rows


def find_splits(x, y, grid, split_coords):
    print(f"finding split from x: {x}, y: {y}")
    # split_coords = set()

    split_found = False
    while (x != len(grid) - 1 and 0 <= y < len(grid[0])) and not split_found:
        x += 1
        char = grid[x][y]
        if char == "^":
            print(f"split! [{x}, {y}]")
            if (x, y) in split_coords:
                print(f"** {x}, {y} has already been visited")
                return set()
            split_found = True
            split_coords.add((x, y))
            splits_left = find_splits(x, y - 1, grid, split_coords)
            split_coords.update(splits_left)
            splits_right = find_splits(x, y + 1, grid, split_coords)
            split_coords.update(splits_right)
            # print(f"splits_left of {x, y}: {splits_left}")
            # print(f"splits_right of {x, y}: {splits_right}")

    print(f"split_coord: {split_coords}")
    print()
    return split_coords


def part_one(grid) -> int:
    starting_idx = 0
    for y in range(len(grid[0])):
        if grid[0][y] == "S":
            starting_idx = y
    print(f"starting_idx: {starting_idx}")
    split_coords = set()
    coords = find_splits(0, starting_idx, grid, split_coords)
    return len(coords)


def main():
    grid = parse_input()
    for i, row in enumerate(grid):
        print(f"{i} {row}")

    part_one_answer = part_one(grid)
    print()
    print(f"part one: {part_one_answer}")


main()
