"""
"""

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 6, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        return input_data

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for i in range(3, len(parsed_data)):
            if len(set(parsed_data[i - 3 : i + 1])) == 4:
                return i + 1
        return -1

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for i in range(13, len(parsed_data)):
            if len(set(parsed_data[i - 13 : i + 1])) == 14:
                return i + 1
        return -1
