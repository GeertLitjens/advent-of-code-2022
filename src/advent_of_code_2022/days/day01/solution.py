"""
Good to start everything up again, I actually spent most time on setting up a way to excessive
Python environment including type checking, linting, formatting and the like.
"""
import numpy as np

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 1, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        The task for today itself was pretty trivial, we simply needed to parse
        the kcal for the individual elfs by splitting on newlines.
        """
        kcal_per_elf = []
        kcal_cur_elf = []
        for line in input_data.splitlines():
            if line:
                kcal_cur_elf.append(int(line))
            else:
                kcal_per_elf.append(kcal_cur_elf)
                kcal_cur_elf = []
        kcal_per_elf.append(kcal_cur_elf)
        return kcal_per_elf

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        This is simply sum kcal per elf and find the max. Very simple to
        handle with Python lists and numpy.
        """
        return np.max([np.sum(kcal_elf) for kcal_elf in parsed_data])

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        This was not anymore difficult than the previous part, just needed
        to sort the list with the total values per elf and take the top 3.
        """
        sum_kcals_per_elf = sorted([np.sum(kcal_elf) for kcal_elf in parsed_data])
        return np.sum(sum_kcals_per_elf[-3:])
