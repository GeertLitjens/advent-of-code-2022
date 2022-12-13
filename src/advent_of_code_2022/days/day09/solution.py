"""
Nice task, essentially implementing Snake, which was pretty cool! The first
task was pretty straightforward, just check the distance to the head and
correct it by moving in the direction. For part 2, I made a mistake initially,
but I'll get to that.
"""

import numpy as np

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 9, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        Split the lines and then the instructions in direction and number of
        steps.
        """
        return [
            (int(instruction.split(" ")[1]), instruction.split(" ")[0])
            for instruction in input_data.splitlines()
        ]

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Pretty straightforward, as soon the distance between the head and the
        body is larger than 1, move in the direction of the difference. And
        use a set to keep track of unique positions.
        """
        rope_pos = np.zeros((2, 2))
        positions = set()

        def update_tail_pos(h: np.array, t: np.array) -> None:
            d = h - t
            if any(np.abs(d) == 2):
                t += np.sign(d)
            return t

        for instruction in parsed_data:
            for _i in range(instruction[0]):
                if instruction[1] == "R":
                    rope_pos[0, 0] += 1
                elif instruction[1] == "L":
                    rope_pos[0, 0] -= 1
                elif instruction[1] == "U":
                    rope_pos[0, 1] += 1
                else:
                    rope_pos[0, 1] -= 1
                update_tail_pos(rope_pos[0], rope_pos[1])
                positions.add(tuple(rope_pos[-1]))
        return len(positions)

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Same trick, but iteratively update the body parts. What I forgot
        initially is that in part 1, the head cannot move diagonally, but the
        body parts can, so my initial solution didn't deal with that correctly.
        I fixed it soon afterwards, and then it worked.
        """

        rope_pos = np.zeros((10, 2))
        positions = set()

        def update_tail_pos(h: np.array, t: np.array) -> None:
            d = h - t
            if any(np.abs(d) == 2):
                t += np.sign(d)
            return t

        for instruction in parsed_data:
            for _i in range(instruction[0]):
                if instruction[1] == "R":
                    rope_pos[0, 0] += 1
                elif instruction[1] == "L":
                    rope_pos[0, 0] -= 1
                elif instruction[1] == "U":
                    rope_pos[0, 1] += 1
                else:
                    rope_pos[0, 1] -= 1
                for p in range(0, rope_pos.shape[0] - 1):
                    update_tail_pos(rope_pos[p], rope_pos[p + 1])
                positions.add(tuple(rope_pos[-1]))
        return len(positions)
