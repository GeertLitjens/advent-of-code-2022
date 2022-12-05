"""
"""

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 5, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        start_pos, instructions_string = input_data.split("\n\n")
        stacks_strings = start_pos.splitlines()
        nr_stacks = int(stacks_strings[-1][-2:])
        stacks = [[] for x in range(nr_stacks)]
        for i in range(len(stacks_strings) - 2, -1, -1):
            stacks_line = stacks_strings[i]
            for j in range(1, len(stacks_line), 4):
                if stacks_line[j] != " ":
                    stacks[j // 4].append(stacks_line[j])

        instructions = []
        for instruction in instructions_string.splitlines():
            first = int(instruction.split("move")[1].split("from")[0])
            second = int(instruction.split("from")[1].split("to")[0])
            third = int(instruction.split("to")[1])
            instructions.append([first, second, third])
        return stacks, instructions

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        stacks, instructions = parsed_data
        for instruction in instructions:
            for _ in range(instruction[0]):
                crate = stacks[instruction[1] - 1].pop()
                stacks[instruction[2] - 1].append(crate)
        top_crates = "".join([stack[-1] for stack in stacks if stack[-1]])
        return top_crates

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        stacks, instructions = parsed_data
        for instruction in instructions:
            crates = []
            for _ in range(instruction[0]):
                if stacks[instruction[1] - 1]:
                    crates.insert(0, stacks[instruction[1] - 1].pop())
            stacks[instruction[2] - 1].extend(crates)
        top_crates = "".join([stack[-1] for stack in stacks if stack[-1]])
        return top_crates
