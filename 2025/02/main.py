class Range:
    def __init__(self, first_id: int, second_id: int):
        self.first_id = first_id
        self.second_id = second_id


def parse_input():
    ranges = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            raw_ranges = line.split(",")
            for raw_range in raw_ranges:
                first_id, second_id = raw_range.split("-")
                ranges.append(Range(int(first_id), int(second_id)))
    return ranges


def part_one(ranges: list[Range]) -> int:
    invalid_ids = []
    for product_id_range in ranges:
        full_range = range(product_id_range.first_id, product_id_range.second_id + 1)

        for r in full_range:
            r_length = len(str(r))
            if r_length % 2 == 0:
                mid_point = r_length // 2
                first_part = str(r)[:mid_point]
                second_part = str(r)[mid_point:]

                is_invalid = True
                for i in range(len(first_part)):
                    if first_part[i] != second_part[i]:
                        is_invalid = False

                if is_invalid:
                    invalid_ids.append(r)
                    print()
                    print("**")
                    print(f"invalid id found: {r}")
                    print()

    return sum(invalid_ids)


def part_two(ranges: list[Range]) -> int:
    invalid_ids = []
    for product_id_range in ranges:
        full_range = range(product_id_range.first_id, product_id_range.second_id + 1)

        for r in full_range:
            r_length = len(str(r))
            factorials = find_factorials(r_length)
            for factorial in factorials:
                parts = split_string(str(r), factorial)
                first_part = parts[0]
                if first_part * (r_length // factorial) == str(r):
                    invalid_ids.append(r)
                    print()
                    print("**")
                    print(f"invalid id found: {r}")
                    print()
                    break

    return sum(invalid_ids)


# length=6 -> [1, 2, 3]
# length=4 -> [1, 2]
def find_factorials(length: int) -> list[int]:
    factorials = []
    r = range(1, length)
    for i in r:
        if length % i == 0:
            factorials.append(i)

    return factorials


# s="123123" factorial=2 -> ["123", "123"]
# s="123123" factorial=3 -> ["12", "31", "23"]
def split_string(s: str, factorial: int) -> list[str]:
    parts = []
    temp = ""
    for char in s:
        temp += char
        if len(temp) == factorial:
            parts.append(temp)
            temp = ""

    return parts


def main():
    ranges = parse_input()
    # part_one_answer = part_one(ranges)
    part_two_answer = part_two(ranges)
    print()
    # print(f"part 1: {part_one_answer}")
    print(f"part 2: {part_two_answer}")


main()
