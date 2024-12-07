from tqdm import tqdm

def setup(lines: list[str]):
    max_y = len(lines)
    max_x = len(lines[0].strip())
    obstacles = []
    starting_position = -1-1j
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == ".":
                continue
            elif char == "#":
                obstacles.append(complex(x, y))
            elif char == "^":
                starting_position = complex(x, y)
    assert starting_position != -1-1j

    return obstacles, starting_position, max_x, max_y

def find_obstacle(obstacles: list[complex], curr: complex, direction: complex, max_x: int, max_y: int):
    n_steps_to_check = (max_x if direction.imag == 0 else max_y)
    for n in range(n_steps_to_check):
        possible_obstacle = curr + (n*direction)
        if possible_obstacle in obstacles:
            return possible_obstacle
    # No obstacles found, set to outside the perimeter
    if direction == 1j:
        # going down
        return complex(curr.real, max_y+1)
    elif direction == -1:
        # going left
        return complex(-2, curr.imag)
    elif direction == -1j:
        # going up
        return complex(curr.real, -2)
    elif direction == 1:
        # going right
        return complex(max_x + 1, curr.imag)
    else:
        ValueError("wrong direction, idiot")


def simulate(obstacles: list[complex], starting_position: complex, max_x: int, max_y:int):

    curr = starting_position
    direction = -1j
    visited = set([(starting_position, direction)])
    while (0 <= curr.real < max_x) and (0 <= curr.imag < max_y): # outside perimeter, or cycle detected
        obstacle = find_obstacle(obstacles, curr, direction, max_x, max_y)
        new_pos = obstacle - direction # always one block away from the obstacle
        steps = ((new_pos - curr) / direction).real
        to_add = [(curr + (i*direction), direction) for i in range(0, int(steps))]
        visited = visited.union(to_add)

        curr = new_pos
        direction = direction * 1j
        if (new_pos, direction) in visited:
            return set([item for item, _ in visited]), True
        
    return set([item for item, _ in visited]), False

if __name__ == "__main__":
    inputs_ = "inputs/day6.txt"
    # inputs_ = "test_inputs/day6.txt"
    # inputs_ = "test_inputs/day6test.txt"
    with open(inputs_) as f:
        lines = f.readlines()
    
    obstacles, starting_position, max_x, max_y = setup(lines)
    visited, is_cycle = simulate(obstacles, starting_position, max_x, max_y)
    # part 1
    print(len(visited))
    
    total = 0
    for has_been_here in tqdm((visited - set([starting_position]))):
        new_obstacles = obstacles + [has_been_here]
        new_path, is_cycle = simulate(new_obstacles, starting_position, max_x, max_y)
        total += is_cycle
    print(total) 
