"""
A very slight upgrade in difficulty today, at least in terms of how to implement
the solution efficiently. Specifically, to quickly identify the items that appear
in multiple strings, we use set intersections. With that, the problem becomes easy
to solve.
"""

import string

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 3, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        Simply parse the input into lines for different rugsacks.
        """
        return input_data.splitlines()

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Step one is to split each rugsack into their compartments, which is just
        right down the middle of the string. Subsequently we look at the set
        intersection of the two compartments to identify the overlapping item
        We then use ASCII indexing to find the corresponding number.
        """
        sum_priorities = 0
        for rugsack in parsed_data:
            compartment1 = rugsack[: len(rugsack) // 2]
            compartment2 = rugsack[len(rugsack) // 2 :]
            (overlap,) = set(compartment1).intersection(set(compartment2))
            if overlap.isupper():
                sum_priorities += string.ascii_uppercase.index(overlap) + 27
            else:
                sum_priorities += string.ascii_lowercase.index(overlap) + 1
        return sum_priorities

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Straightforward extension of part 1, we simply iterate over the list
        of rugsacks with steps of three and take the intersection of all three
        """
        sum_priorities = 0
        for i in range(0, len(parsed_data), 3):
            (badge,) = set.intersection(
                set(parsed_data[i]), set(parsed_data[i + 1]), set(parsed_data[i + 2])
            )
            if badge.isupper():
                sum_priorities += string.ascii_uppercase.index(badge) + 27
            else:
                sum_priorities += string.ascii_lowercase.index(badge) + 1
        return sum_priorities
