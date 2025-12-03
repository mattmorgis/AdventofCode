from typing import Literal, Tuple


class Rotation:
    def __init__(self, direction: Literal["R", "L"], distance: int):
        self.direction = direction
        self.distance = distance


def parse_input() -> list[Rotation]:
    rotations = []
    with open("input-test.txt") as file:
        while line := file.readline().rstrip():
            direction = line[0]
            distance = int(line[1:])
            rotation = Rotation(direction, distance)
            rotations.append(rotation)
    return rotations


def day_one(rotations: list[Rotation]) -> Tuple[int, int]:
    start = 0
    current = 50
    end = 100
    ends_on_zero = 0
    passes_zero = 0

    for rotation in rotations:
        print(
            f"Rotation.direction: {rotation.direction} \t Rotation.distance: {rotation.distance}"
        )

        if rotation.direction == "R":
            new_pos = current + rotation.distance
            if new_pos >= 100:
                passes_zero += new_pos // 100
                print(f"**passes zero R: {passes_zero}")
            current = new_pos % 100
        else:
            new_pos = current - rotation.distance
            if new_pos <= 0:
                if new_pos == 0:
                    passes_zero += 1
                else:
                    passes_zero += abs(new_pos // 100)
                print(f"**passes zero L: {passes_zero}")
            current = new_pos % 100

        print(f"current dial: {current}")

        if current == 0:
            ends_on_zero += 1
            print(f"**lands on zero: {ends_on_zero}")

    return (ends_on_zero, passes_zero)


def main():
    rotations = parse_input()
    part_one, part_two = day_one(rotations)
    print()
    print(f"Part One Answer: {part_one}")
    print(f"Part Two Answer: {part_two}")


main()
