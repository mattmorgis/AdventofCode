from dataclasses import dataclass
from math import sqrt, prod


@dataclass
class Coord:
    x: int
    y: int
    z: int


@dataclass
class CoordPair:
    coord_1: Coord
    coord_2: Coord
    distance: float = 0


def parse_input() -> list[Coord]:
    coords = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            x, y, z = line.split(",")
            coords.append(Coord(int(x), int(y), int(z)))
    return coords


def find_pairs(coords: list[Coord]) -> list[CoordPair]:
    pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            pairs.append(CoordPair(coords[i], coords[j]))
    return pairs


def find_distance(coord_1: Coord, coord_2: Coord) -> float:
    x = (coord_2.x - coord_1.x) ** 2
    y = (coord_2.y - coord_1.y) ** 2
    z = (coord_2.z - coord_1.z) ** 2

    return sqrt(x + y + z)


def build_circuits(coords: list[Coord]):
    coord_pairs = find_pairs(coords)
    for pair in coord_pairs:
        pair.distance = find_distance(pair.coord_1, pair.coord_2)
    coord_pairs.sort(key=lambda x: x.distance)

    # top_k = coord_pairs[:50]
    # for i, pair in enumerate(top_k):
    #     print(f"{i}: {pair}")
    #     if pair.coord_1.x == 216 and pair.coord_2.x == 117:
    #         print(f"winner found at index {i}")
    #     if pair.coord_1.x == 117 and pair.coord_2.x == 216:
    #         print(f"winner found at index {i}")

    circuits: list[set[tuple[int, int, int]]] = []
    coord_set = set([(c.x, c.y, c.z) for c in coords])

    # print(f"coord_set: {coord_set}")
    x = 0
    y = 0
    for k, pair in enumerate(coord_pairs):
        coord_1 = (pair.coord_1.x, pair.coord_1.y, pair.coord_1.z)
        coord_2 = (pair.coord_2.x, pair.coord_2.y, pair.coord_2.z)
        print(f"coord_1: {coord_1}")
        print(f"coord_2: {coord_2}")

        coord_1_match = -1
        coord_2_match = -1

        for i, circuit in enumerate(circuits):
            if coord_1 in circuit:
                coord_1_match = i
            if coord_2 in circuit:
                coord_2_match = i
        if coord_1_match >= 0 and coord_2_match <= 0:
            circuits[coord_1_match].update([coord_1, coord_2])
        if coord_2_match >= 0 and coord_1_match <= 0:
            circuits[coord_2_match].update([coord_1, coord_2])
        if coord_1_match >= 0 and coord_2_match >= 0:
            if coord_1_match == coord_2_match:
                continue
            circuits[coord_1_match].update(circuits[coord_2_match])
            del circuits[coord_2_match]
        if coord_1_match < 0 and coord_2_match < 0:
            circuits.append({coord_1, coord_2})

        if coord_1 in coord_set:
            coord_set.remove(coord_1)
        if coord_2 in coord_set:
            coord_set.remove(coord_2)

        print("circuits:")
        for cir in circuits:
            print(cir)

        if len(circuits) == 1 and len(coord_set) == 0:
            print(f"** winner in index {k}: {coord_1}, {coord_2}")
            x = coord_1[0]
            y = coord_2[0]
            break
        # lengths = [len(cir) for cir in circuits]
        # lengths.sort(reverse=True)
        # print(f"3 longest circuits lengths: {lengths[:3]}")
        print()
    # return prod(lengths[:3])
    return x * y


def main():
    coords = parse_input()
    print(f"coords len: {len(coords)}")

    answer = build_circuits(coords)
    print(f"answer: {answer}")


main()
