import numpy as np
from itertools import product


def check_horizontal(lines):
    total = 0
    for i in range(lines.shape[0]):
        total += sum(
            "".join(lines[i, j : j + 4]) == "XMAS" for j in range(lines.shape[1] - 3)
        )
    return total


def check_vertical(lines):
    total = 0
    for j in range(lines.shape[1]):
        total += sum(
            "".join(lines[i : i + 4, j]) == "XMAS" for i in range(lines.shape[0] - 3)
        )
    return total


def check_diagonal(lines):
    total = 0
    for i, j in product(range(lines.shape[0] - 3), range(lines.shape[1] - 3)):
        if (
            "".join(
                [
                    lines[i, j],
                    lines[i + 1, j + 1],
                    lines[i + 2, j + 2],
                    lines[i + 3, j + 3],
                ]
            )
            == "XMAS"
        ):
            total += 1
    return total


def part1(lines: np.ndarray):
    horizontal = check_horizontal(lines) + check_horizontal(np.fliplr(lines))
    vertical = check_vertical(lines) + check_vertical(np.flipud(lines))
    diagonal = (
        check_diagonal(lines)
        + check_diagonal(np.fliplr(lines))
        + check_diagonal(np.flipud(lines))
        + check_diagonal(np.fliplr(np.flipud(lines)))
    )
    print(horizontal)
    print(vertical)
    print(diagonal)
    print(horizontal + vertical + diagonal)


def check_x_mas(lines: np.ndarray):
    to_match = np.array(
        [
            ["M", ".", "S"],
            [".", "A", "."],
            ["M", ",", "S"],
        ]
    )
    important_mask = (np.eye(3) + np.fliplr(np.eye(3))) > 0  # cursed x mask creation
    total = 0
    for i, j in product(range(1, lines.shape[0]-1), range(1, lines.shape[1]-1)):
        matching = lines[i - 1 : i + 2, j - 1 : j + 2] == to_match
        if (matching * important_mask).sum() == 5:
            total += 1
    return total


def part2(lines: np.ndarray):

    total = (
        check_x_mas(lines)
        + check_x_mas(np.rot90(lines, k=1))
        + check_x_mas(np.rot90(lines, k=2))
        + check_x_mas(np.rot90(lines, k=3))
    )
    print(total)


if __name__ == "__main__":
    input_ = "inputs/day4.txt"
    # input_ = "test_inputs/day4.txt"
    with open(input_) as f:
        lines = f.readlines()
        lines = [[char for char in line.strip()] for line in lines]
        lines = np.array(lines)

    part1(lines)
    part2(lines)
