import os

def part1(lines):
    print(
        sum(
            abs(x - y)
            for x, y in zip(
                sorted([x[0] for x in lines]), sorted([x[1] for x in lines])
            )
        )
    )


def part2(lines):
    print(
        sum(
            item[0] * sum(x[1] == item[0]for x in lines) for item in lines
        )
    )


if __name__ == "__main__":
    with open("inputs/day1.txt") as f:
        lines = f.readlines()
        lines = [tuple(map(int, x.split("   "))) for x in lines]
    part1(lines)
    part2(lines)
