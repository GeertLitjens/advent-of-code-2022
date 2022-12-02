"""
"""
from advent_of_code_2022.utils import AoCData, Solution

scoring_1 = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6},
}

scoring_2 = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 2, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        return [x.split(" ") for x in input_data.splitlines()]

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        score = 0
        for round in parsed_data:
            score += scoring_1[round[0]][round[1]]
        return score

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        score = 0
        for round in parsed_data:
            score += scoring_2[round[0]][round[1]]
        return score
