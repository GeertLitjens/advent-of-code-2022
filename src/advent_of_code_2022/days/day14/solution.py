"""
"""

import numpy as np

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 14, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        paths = input_data.splitlines()
        xs = []
        ys = []
        for path in paths:
            coords = path.split(" -> ")
            xs.extend([int(coord.split(",")[0]) for coord in coords])
            ys.extend([int(coord.split(",")[1]) for coord in coords])
        col_min = min(xs)
        col_max = max(xs)
        row_max = max(ys)
        cave = np.zeros((row_max + 1, col_max - col_min + 1), dtype="ubyte")
        for path in paths:
            coords = path.split(" -> ")
            for i, coord in enumerate(coords[:-1]):
                x1, y1 = [int(x) for x in coord.split(",")]
                x2, y2 = [int(x) for x in coords[i + 1].split(",")]
                if x1 == x2:
                    cave[
                        min(y1, y2) : max(y1, y2) + 1,
                        x1 - col_min,
                    ] = 1
                else:
                    cave[y1, min(x1, x2) - col_min : max(x1, x2) - col_min + 1] = 1
        return cave, 500 - col_min

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        cave, sand_pos = parsed_data
        prev_sand = -1
        while np.sum(cave == 2) != prev_sand:
            prev_sand = np.sum(cave == 2)
            cur_pos = [0, sand_pos]
            while True:
                if cur_pos[0] + 1 >= cave.shape[0]:
                    break
                if cave[cur_pos[0] + 1, cur_pos[1]] == 0:
                    cur_pos[0] += 1
                    continue
                else:
                    if cur_pos[1] - 1 < 0:
                        break
                    elif cave[cur_pos[0] + 1, cur_pos[1] - 1] == 0:
                        cur_pos[0] += 1
                        cur_pos[1] -= 1
                    elif cur_pos[1] + 1 >= cave.shape[1]:
                        break
                    elif cave[cur_pos[0] + 1, cur_pos[1] + 1] == 0:
                        cur_pos[0] += 1
                        cur_pos[1] += 1
                    else:
                        cave[cur_pos[0], cur_pos[1]] = 2
                        break
        return np.sum(cave == 2)

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        cave, sand_pos = parsed_data
        total_depth = cave.shape[0] + 2
        cave = np.pad(cave, ((0, 2), (total_depth, total_depth)))
        sand_pos += total_depth
        cave[-1, :] = 1
        while cave[0, sand_pos] != 2:
            cur_pos = [0, sand_pos]
            while True:
                if cur_pos[0] + 1 >= cave.shape[0]:
                    break
                if cave[cur_pos[0] + 1, cur_pos[1]] == 0:
                    cur_pos[0] += 1
                    continue
                else:
                    if cur_pos[1] - 1 < 0:
                        break
                    elif cave[cur_pos[0] + 1, cur_pos[1] - 1] == 0:
                        cur_pos[0] += 1
                        cur_pos[1] -= 1
                    elif cur_pos[1] + 1 >= cave.shape[1]:
                        break
                    elif cave[cur_pos[0] + 1, cur_pos[1] + 1] == 0:
                        cur_pos[0] += 1
                        cur_pos[1] += 1
                    else:
                        cave[cur_pos[0], cur_pos[1]] = 2
                        break
        return np.sum(cave == 2)
