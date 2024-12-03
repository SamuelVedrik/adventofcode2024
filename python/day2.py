
def is_decreasing_safe(line):
    return all((x < y) and (abs(x-y) <= 3) for x, y in zip(line[:-1], line[1:]))

def is_increasing_safe(line):
    return all((x > y) and (abs(x-y) <= 3) for x, y in zip(line[:-1], line[1:]))

def part1(lines):
    num_safe = 0
    for line in lines:
        num_safe += (is_decreasing_safe(line) or is_increasing_safe(line))
    print(num_safe)

def part2(lines):
    num_safe = 0
    for line in lines:
        is_decreasing_safe_remove_1 = any(
            is_decreasing_safe(line[:i] + line[i+1:]) for i in range(len(line))
        ) or is_decreasing_safe(line)
        is_increasing_safe_remove_1 = any(
            is_increasing_safe(line[:i] + line[i+1:]) for i in range(len(line)) 
        ) or is_increasing_safe(line)

        num_safe += (is_decreasing_safe_remove_1 or is_increasing_safe_remove_1)
    print(num_safe)

if __name__ == '__main__':

    with open("inputs/day2.txt") as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.split(" ")] for line in lines]
    
    part1(lines)
    part2(lines)