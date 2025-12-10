def parse_input():
    coords = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            x, y = line.split(",")
            coords.append((int(x), int(y)))
    return coords


def find_pairs(coords):
    pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            pairs.append([coords[i], coords[j]])
    return pairs


def part_one(coords):
    pairs = find_pairs(coords)
    largest_area = 0
    for pair in pairs:
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]
        l = (abs(x2 - x1)) + 1
        w = (abs(y2 - y1)) + 1
        area = l * w
        print(f"pair: {pair}, area: {area}")
        print()
        if area > largest_area:
            largest_area = area

    return largest_area


def main():
    coords = parse_input()
    part_one_ans = part_one(coords)
    print()
    print(f"part one: {part_one_ans}")


main()
