def part_one() -> int:
    count = 1
    jolts: list[int] = []
    with open("input-test.txt") as file:
        while line := file.readline().rstrip():
            print(f"new bank: {line}")
            max_jolt = 0
            for i in range(0, len(line)):
                for j in range(i + 1, len(line)):
                    jolt = int(line[i] + line[j])
                    if jolt > max_jolt:
                        max_jolt = jolt
                    elif j - i == 1:
                        break
            print(f"line finished, found max_jolt: {max_jolt}")
            jolts.append(max_jolt)
    print(f"count = {count}")
    return sum(jolts)


def part_two() -> int:
    jolts: list[int] = []
    with open("input.txt") as file:
        while line := file.readline().rstrip():
            print(f"new bank: {line}")

            stack: list[int] = []
            batteries_left_in_bank = len(line)

            for battery in line:
                charge = int(battery)
                print(f"charge: {charge}")

                while stack and charge > stack[-1]:
                    spaces_to_fill = 12 - len(stack)
                    if batteries_left_in_bank > spaces_to_fill:
                        stack.pop()
                    else:
                        break

                if len(stack) < 12:
                    stack.append(charge)

                batteries_left_in_bank -= 1
                print(f"batteries left: {batteries_left_in_bank}, stack: {stack}")

            max_jolt = int("".join(map(str, stack)))
            print(f"line finished, found max_jolt: {max_jolt}")
            jolts.append(max_jolt)
            print()
    return sum(jolts)


def main():
    # part_one_answer = part_one()
    part_two_answer = part_two()
    print()
    # print(f"part 1: {part_one_answer}")
    print(f"part 2: {part_two_answer}")


main()
