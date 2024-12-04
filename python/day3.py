import re
import numpy as np

def part1(text):
    matches = re.findall(r"mul\([\d]+,[\d]+\)", text)
    total = 0
    for match in matches:
        left, right = match.replace("mul", "").strip("()").split(",")
        total += (int(left) * int(right))
    print(total)

def part2(text):
    muls = list(re.finditer(r"mul\([\d]+,[\d]+\)", text))
    dos = list(re.finditer(r"do\(\)", text))
    donts = list(re.finditer(r"don't\(\)", text))
    action_dict = {}
    starts = []
    for match in dos:
        action_dict[match.start()] = True
        starts.append(match.start())
    for match in donts:
        action_dict[match.start()] = False
        starts.append(match.start())
    starts = sorted(starts)
    
    muls_positions = [match.start() for match in muls]
    perform_mult = [action_dict[starts[i-1]] if i > 0 else True for i in np.searchsorted(starts, muls_positions)]

    total = 0
    for match, perform in zip(muls, perform_mult):
        left, right = match.group(0).replace("mul", "").strip("()").split(",")
        if perform:
            total += (int(left) * int(right))
    
    print(total)



if __name__ == "__main__":
    with open("inputs/day3.txt") as f :
        lines = f.readlines()
        text = "".join(lines)
    
    # part1(text)
    part2(text)