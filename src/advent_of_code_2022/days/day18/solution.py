"""
"""

import numpy as np
from skimage.segmentation import flood_fill

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 18, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        max_x, max_y, max_z = 0, 0, 0
        poss = []
        for line in input_data.splitlines():
            poss.append([int(x) for x in line.split(",")])
            if (x := poss[-1][0]) > max_x:
                max_x = x
            if (y := poss[-1][1]) > max_y:
                max_y = y
            if (z := poss[-1][2]) > max_z:
                max_z = z
        field = np.zeros((max_x + 3, max_y + 3, max_z + 3), dtype="byte")
        for pos in poss:
            field[pos[0] + 1, pos[1] + 1, pos[2] + 1] = 1
        return field

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        open_sides = 0
        for z in range(1, parsed_data.shape[2] - 1):
            for y in range(1, parsed_data.shape[1] - 1):
                for x in range(1, parsed_data.shape[0] - 1):
                    if parsed_data[x, y, z] == 1:
                        open_sides += (
                            6
                            - parsed_data[x - 1, y, z]
                            - parsed_data[x + 1, y, z]
                            - parsed_data[x, y - 1, z]
                            - parsed_data[x, y + 1, z]
                            - parsed_data[x, y, z - 1]
                            - parsed_data[x, y, z + 1]
                        )
        return open_sides

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        filled_space = parsed_data + (
            np.abs(flood_fill(parsed_data, (0, 0, 0), connectivity=1, new_value=1) - 1)
        )
        open_sides = 0
        for z in range(1, filled_space.shape[2] - 1):
            for y in range(1, filled_space.shape[1] - 1):
                for x in range(1, filled_space.shape[0] - 1):
                    if filled_space[x, y, z] == 1:
                        open_sides += (
                            6
                            - filled_space[x - 1, y, z]
                            - filled_space[x + 1, y, z]
                            - filled_space[x, y - 1, z]
                            - filled_space[x, y + 1, z]
                            - filled_space[x, y, z - 1]
                            - filled_space[x, y, z + 1]
                        )
        return open_sides
