from collections import namedtuple
import heapq

Problem = namedtuple("Problem", ["target", "variables"])


def parse_inputs(lines: list[str]):
    problems = []
    for line in lines:
        target, variables = line.split(": ")
        variables = [int(item) for item in variables.split(" ")]
        problems.append(Problem(int(target), variables))

    return problems

def try_solve_problem(problem: Problem, with_concat_state=False):
    
    queue = [(abs(problem.target - problem.variables[0]), problem.variables[0], 0, f"({problem.variables[0]})")] # distance to target used as heuristic
    while len(queue) != 0:
        (distance, curr_state, index, sol) = heapq.heappop(queue)
        if (curr_state == problem.target) and (index == len(problem.variables) - 1):
            return problem.target, sol
        if index >= len(problem.variables) - 1: # no more adding if no children to add
            continue
        # add children
        next_var = problem.variables[index+1]
        add_state = curr_state + next_var
        mult_state = curr_state * next_var
        concat_state =int(f"{curr_state}{next_var}")
        heapq.heappush(queue, (abs(problem.target - add_state), add_state, index+1, f"({sol}+{next_var})"))
        heapq.heappush(queue, (abs(problem.target - mult_state), mult_state, index+1, f"({sol}*{next_var})"))
        if with_concat_state: 
            heapq.heappush(queue, (abs(problem.target - concat_state), concat_state, index+1, f"({sol}||{next_var})"))

    return -1, "" # not found
    

if __name__ == "__main__":

    # inputs = "test_inputs/day7.txt"
    inputs = "inputs/day7.txt"
    with open(inputs) as f:
        lines = f.readlines() 
        lines = [line.strip() for line in lines]

    problems = parse_inputs(lines)
    part1_result = 0
    part2_result = 0
    for problem in problems:
        problem_result, _ = try_solve_problem(problem)
        problem_result2, _ = try_solve_problem(problem, with_concat_state=True)
        if problem_result != -1: # solved
            part1_result += problem.target
        if problem_result2 != -1:
            part2_result += problem.target

    print(part1_result)
    print(part2_result)