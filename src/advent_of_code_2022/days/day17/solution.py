"""
"""
import numpy as np

from advent_of_code_2022.utils import AoCData, Solution

ROCKS = [
    np.array([[1, 1, 1, 1]], dtype="ubyte"),
    np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype="ubyte"),
    np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]], dtype="ubyte"),
    np.array([[1], [1], [1], [1]], dtype="ubyte"),
    np.array([[1, 1], [1, 1]], dtype="ubyte"),
]


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 17, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        return [x for x in input_data if x != "\n"]

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        playing_field = np.zeros((2023 * 4, 9), dtype="ubyte")
        playing_field[:, 0] = 1
        playing_field[:, 8] = 1
        playing_field[0, :] = 1
        cur_height = 0
        j = 0
        for i in range(2022):
            cur_rock = ROCKS[i % 5]
            off_x = 3
            rock_height, rock_width = cur_rock.shape
            off_y = rock_height + cur_height + 3
            while True:
                jet_dir = parsed_data[j % len(parsed_data)]
                j += 1
                if (
                    jet_dir == ">"
                    and (
                        playing_field[
                            off_y - rock_height + 1 : off_y + 1,
                            off_x + 1 : off_x + rock_width + 1,
                        ]
                        + cur_rock
                        < 2
                    ).all()
                ):
                    off_x += 1
                elif (
                    jet_dir == "<"
                    and (
                        playing_field[
                            off_y - rock_height + 1 : off_y + 1,
                            off_x - 1 : off_x + rock_width - 1,
                        ]
                        + cur_rock
                        < 2
                    ).all()
                ):
                    off_x -= 1
                if (
                    (
                        playing_field[
                            off_y - rock_height : off_y, off_x : off_x + rock_width
                        ]
                        + cur_rock
                    )
                    > 1
                ).any():
                    playing_field[
                        off_y - rock_height + 1 : off_y + 1, off_x : off_x + rock_width
                    ] += cur_rock
                    if off_y > cur_height:
                        cur_height = off_y
                    break
                else:
                    off_y -= 1
        return cur_height

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        playing_field = np.zeros((20000 * 4, 9), dtype="ubyte")
        playing_field[:, 0] = 1
        playing_field[:, 8] = 1
        playing_field[0, :] = 1
        cur_height = 0
        j = 0
        offset = 1_000_000_000_000 - (((1_000_000_000_000 - 175) // 1740) * 1740) - 175
        for i in range(175 + offset):
            cur_rock = ROCKS[i % 5]
            off_x = 3
            rock_height, rock_width = cur_rock.shape
            off_y = rock_height + cur_height + 3
            while True:
                jet_dir = parsed_data[j % len(parsed_data)]
                j += 1
                if (
                    jet_dir == ">"
                    and (
                        playing_field[
                            off_y - rock_height + 1 : off_y + 1,
                            off_x + 1 : off_x + rock_width + 1,
                        ]
                        + cur_rock
                        < 2
                    ).all()
                ):
                    off_x += 1
                elif (
                    jet_dir == "<"
                    and (
                        playing_field[
                            off_y - rock_height + 1 : off_y + 1,
                            off_x - 1 : off_x + rock_width - 1,
                        ]
                        + cur_rock
                        < 2
                    ).all()
                ):
                    off_x -= 1
                if (
                    (
                        playing_field[
                            off_y - rock_height : off_y, off_x : off_x + rock_width
                        ]
                        + cur_rock
                    )
                    > 1
                ).any():
                    playing_field[
                        off_y - rock_height + 1 : off_y + 1, off_x : off_x + rock_width
                    ] += cur_rock
                    if off_y > cur_height:
                        cur_height = off_y
                    key = (
                        str(i % 5)
                        + "_"
                        + str(j % len(parsed_data))
                        + "_"
                        + "".join([str(x) for x in playing_field[cur_height, :]])
                    )
                    if key == "0_1075_101111001":
                        print(i)
                        print(cur_height)
                    break
                else:
                    off_y -= 1
        cur_height += ((1_000_000_000_000 - 175) // 1740) * 2724
        return cur_height
