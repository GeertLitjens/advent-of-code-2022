"""
Pretty straightforward today, no need for any parsing even. Then use sets
to solve both part's.
"""

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 6, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        No parsing required, just forward the string.
        """
        return input_data

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Iterate over the string, if we have a set that has length 4 we have
        found the start-of-packet.
        """
        for i in range(4, len(parsed_data) + 1):
            if len(set(parsed_data[i - 4 : i])) == 4:
                return i
        return -1

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Exactly the same for part 2, except using 14 tokens instead of 4.
        """
        for i in range(14, len(parsed_data) + 1):
            if len(set(parsed_data[i - 14 : i])) == 14:
                return i
        return -1
