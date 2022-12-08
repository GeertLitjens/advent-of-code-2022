"""
"""

import numpy as np

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 8, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        lines = input_data.splitlines()
        arr_shape = (len(lines), len(lines[0]))
        arr = np.fromstring(
            ",".join(input_data.replace("\n", "")), dtype="int", sep=","
        ).reshape(arr_shape)
        print(arr_shape)
        return arr

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        rows, cols = parsed_data.shape
        nr_vis_trees = 2 * cols + 2 * (rows - 2)
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                cur_height = parsed_data[row, col]
                if (
                    cur_height > np.max(parsed_data[:row, col])
                    or cur_height > np.max(parsed_data[row + 1 :, col])
                    or cur_height > np.max(parsed_data[row, :col])
                    or cur_height > np.max(parsed_data[row, col + 1 :])
                ):
                    nr_vis_trees += 1
        return nr_vis_trees

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        max_score = 0
        rows, cols = parsed_data.shape
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                cur_height = parsed_data[row, col]
                left = parsed_data[row, :col][::-1] >= cur_height
                if left.any():
                    left_trees = np.argmax(left) + 1
                else:
                    left_trees = left.shape[0]
                right = parsed_data[row, col + 1 :] >= cur_height
                if right.any():
                    right_trees = np.argmax(right) + 1
                else:
                    right_trees = right.shape[0]
                up = parsed_data[:row, col][::-1] >= cur_height
                if up.any():
                    up_trees = np.argmax(up) + 1
                else:
                    up_trees = up.shape[0]
                down = parsed_data[row + 1 :, col] >= cur_height
                if down.any():
                    down_trees = np.argmax(down) + 1
                else:
                    down_trees = down.shape[0]
                cur_score = up_trees * down_trees * left_trees * right_trees
                if cur_score > max_score:
                    max_score = cur_score
        return max_score
