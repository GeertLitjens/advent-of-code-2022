"""
Again not too complicated today, just some thinking about hwo to phrase the if
statements. I implemented a lot of this type of code for assessing bounding
box overlaps, so quite straightforward in 1D.
"""
from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 4, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        The parsing was a bit more involved because I wanted to prepare it in ints
        for the subsequent functions. So first split the lines, then the pairs and
        then store the min and max.
        """
        pairs = []
        for line in input_data.splitlines():
            pair1, pair2 = line.split(",")
            pair1_min, pair1_max = pair1.split("-")
            pair2_min, pair2_max = pair2.split("-")
            pairs.append(
                [[int(pair1_min), int(pair1_max)], [int(pair2_min), int(pair2_max)]]
            )
        return pairs

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Two if-statements are needed to check if either pair 1 or 2 are fully
        within the other. Very straightforward.
        """
        complete_overlap = 0
        for pair in parsed_data:
            if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
                complete_overlap += 1
            elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
                complete_overlap += 1
        return complete_overlap

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        I could imagine that this one could have led to some overengineering, but you
        actually only have to check whether the minimum of one of the ranges is within
        the other for both pairs.
        """
        partial_overlap = 0
        for pair in parsed_data:
            if pair[1][1] >= pair[0][0] >= pair[1][0]:
                partial_overlap += 1
            elif pair[0][1] >= pair[1][0] >= pair[0][0]:
                partial_overlap += 1
        return partial_overlap
