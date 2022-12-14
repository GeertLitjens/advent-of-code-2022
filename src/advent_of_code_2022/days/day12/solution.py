"""
"""

import numpy as np

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 12, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        row_strings = input_data.splitlines()
        cols = len(row_strings[0])
        h_map = np.zeros((len(row_strings), cols))
        start_pos, end_pos = ([0, 0], [0, 0])
        for i, row_str in enumerate(row_strings):
            for j, char in enumerate(row_str):
                if char == "S":
                    start_pos = [i, j]
                    h_map[i, j] = 0
                elif char == "E":
                    end_pos = [i, j]
                    h_map[i, j] = 25
                else:
                    h_map[i, j] = ord(char) - 97
        return start_pos, end_pos, h_map

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        start_pos, end_pos, h_map = parsed_data
        paths = [[start_pos]]
        cur_path = []
        visited = [start_pos]
        while paths:
            cur_path = paths.pop(0)
            pth_trm = h_map[cur_path[-1][0], cur_path[-1][1]]
            for nb in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                cur_nb_pos = [cur_path[-1][0] + nb[0], cur_path[-1][1] + nb[1]]
                if (
                    cur_nb_pos[0] < 0
                    or cur_nb_pos[1] < 0
                    or cur_nb_pos in visited
                    or cur_nb_pos[0] >= h_map.shape[0]
                    or cur_nb_pos[1] >= h_map.shape[1]
                ):
                    continue
                cur_nb_val = h_map[cur_nb_pos[0], cur_nb_pos[1]]
                if cur_nb_val - pth_trm <= 1:
                    visited.append(cur_nb_pos)
                    paths.append(cur_path + [cur_nb_pos])
                    if cur_nb_pos == end_pos:
                        return len(cur_path)
        return -1

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        start_pos, end_pos, h_map = parsed_data
        paths = [[start_pos]]
        cur_path = []
        visited = [start_pos]
        path_lengths = []
        while paths:
            cur_path = paths.pop(0)
            pth_trm = h_map[cur_path[-1][0], cur_path[-1][1]]
            for nb in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                cur_nb_pos = [cur_path[-1][0] + nb[0], cur_path[-1][1] + nb[1]]
                if (
                    cur_nb_pos[0] < 0
                    or cur_nb_pos[1] < 0
                    or cur_nb_pos in visited
                    or cur_nb_pos[0] >= h_map.shape[0]
                    or cur_nb_pos[1] >= h_map.shape[1]
                ):
                    continue
                cur_nb_val = h_map[cur_nb_pos[0], cur_nb_pos[1]]
                if cur_nb_val - pth_trm <= 1:
                    if cur_nb_pos == end_pos:
                        path_lengths.append(
                            list(reversed([h_map[x[0], x[1]] for x in cur_path])).index(
                                0
                            )
                            + 1
                        )
                    else:
                        paths.append(cur_path + [cur_nb_pos])
                        visited.append(cur_nb_pos)
        return min(path_lengths)
