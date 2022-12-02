"""
Pretty straightforward first day, with essentially mainly data parsing and
summing / maxing
"""
from typing import Any

import numpy as np

from advent_of_code_2022.utils import Solution


class DaySolution(Solution):
    def __init__(self, day: int = 1, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self, input_data: str) -> Any:
        """
        Simply convert the numbers to ints and making a separate list for each elf
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

    def _solve_part1(self, parsed_data: Any) -> Any:
        """
        Simply iterate over all elves and return the max
        """
        return np.max([np.sum(kcal_elf) for kcal_elf in parsed_data])

    def _solve_part2(self, parsed_data: Any) -> Any:
        """ """
        sum_kcals_per_elf = sorted([np.sum(kcal_elf) for kcal_elf in parsed_data])
        return np.sum(sum_kcals_per_elf[-3:])
