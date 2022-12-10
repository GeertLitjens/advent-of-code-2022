"""
"""

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 10, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        return input_data.splitlines()

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        X = 1
        prev_X = 1
        cycle = 1
        signal_strength = 0
        report_cycles = 20
        for instruction in parsed_data:
            if instruction == "noop":
                cycle += 1
            else:
                prev_X = X
                X += int(instruction.split(" ")[1])
                cycle += 2
                if cycle > report_cycles:
                    signal_strength += report_cycles * prev_X
                    report_cycles += 40
                    if report_cycles > 220:
                        break
        return signal_strength

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        X = 1
        cycle = 1
        instruction_cycles = 0
        crt = ""
        cur_instruction = parsed_data.pop(0)
        while parsed_data:
            if "addx" in cur_instruction and instruction_cycles == 2:
                X += int(cur_instruction.split(" ")[1])
                instruction_cycles = 0
                cur_instruction = cur_instruction = parsed_data.pop(0)
            elif cur_instruction == "noop":
                cur_instruction = cur_instruction = parsed_data.pop(0)
                instruction_cycles = 0
            if X - 1 <= (cycle - 1) % 40 <= X + 1:
                crt += "#"
            else:
                crt += "."
            if cycle % 40 == 0:
                crt += "\n"
            cycle += 1
            instruction_cycles += 1
        return "\n" + crt
