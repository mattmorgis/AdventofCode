from dataclasses import dataclass
from typing import Tuple


@dataclass
class Range:
    start: int
    end: int


def parse_input() -> Tuple[list[Range], list[int]]:
    ranges: list[Range] = []
    ingredients: list[int] = []
    with open("input-test.txt") as file:
        parsing_ranges = True
        while line := file.readline():
            if line == "\n":
                parsing_ranges = False
                continue

            line = line.rstrip()
            if parsing_ranges:
                start, end = line.split("-")
                ranges.append(Range(int(start), int(end)))
            else:
                ingredients.append(int(line))
    return ranges, ingredients


def part_one(ranges: list[Range], ingredients: list[int]) -> int:
    # print(f"ranges: {ranges}")
    # print(f"ingredients: {ingredients}")

    fresh = 0

    for ingredient in ingredients:
        for r in ranges:
            if ingredient >= r.start and ingredient <= r.end:
                # print(f"ingredient {ingredient} is fresh")
                fresh += 1
                break

    return fresh


def overlaps(x: Range, y: Range) -> bool:
    return max(x.start, y.start) <= min(x.end, y.end)


def part_two(ranges: list[Range]) -> int:
    ranges.sort(key=lambda r: r.start)
    for r in ranges:
        print(f"[{r.start} - {r.end}]")
    print()

    fresh: list[Range] = []
    prev: Range
    for i in range(len(ranges)):
        print(f"i: {i}")
        if i == 0:
            prev = ranges[i]
            continue
        curr = ranges[i]
        print(f"prev: {prev}, curr: {curr}")
        if overlaps(prev, curr):
            print("overlaps")
            prev = Range(min(prev.start, curr.start), max(prev.end, curr.end))
            print(f"prev: {prev}")
        else:
            print("no overlap")
            fresh.append(prev)
            prev = curr
        print(f"fresh: {fresh}")
        print()

    fresh.append(prev)
    print()
    print("finished, fresh:")
    count = 0
    for r in fresh:
        print(f"[{r.start} - {r.end}]")
        count += (r.end - r.start) + 1
    return count


def main():
    ranges, ingredients = parse_input()
    part_one_answer = part_one(ranges, ingredients)
    print(f"part one: {part_one_answer}")
    print()
    part_two_answer = part_two(ranges)
    print()
    print(f"part two: {part_two_answer}")


main()
