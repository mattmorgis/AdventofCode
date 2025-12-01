from typing import Literal


class Rotation:
    def __init__(self, direction: Literal["R", "L"], distance: int):
        self.direction = direction
        self.distance = distance


def parse_input() -> list[Rotation]:
    rotations = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            direction = line[0]
            distance = int(line[1:])
            rotation = Rotation(direction, distance)
            rotations.append(rotation)
    return rotations


def part_one(rotations: list[Rotation]) -> int:
    start = 0
    current = 50
    end = 100
    times_at_start = 0

    for rotation in rotations:
        print(
            f"Rotation.direction: {rotation.direction} \t Rotation.distance: {rotation.distance}"
        )
        if rotation.distance > end:
            rotation.distance = rotation.distance % end

        if rotation.direction == "R":
            current = current + rotation.distance
            if current == end:
                current = start
            elif current > end:
                current = abs(end - current)
        else:
            current = current - rotation.distance
            if current < start:
                current = end + current

        print(f"current dial: {current}")

        if current == start:
            times_at_start = times_at_start + 1

    return times_at_start


def main():
    rotations = parse_input()
    part_one_answer = part_one(rotations)
    print()
    print(f"Part One Answer: {part_one_answer}")


main()
