"""
"""
from ast import literal_eval
from functools import cmp_to_key
from typing import Union

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 13, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        all_pairs_str = input_data.split("\n\n")
        pairs = []
        for pairs_str in all_pairs_str:
            pair_lst = pairs_str.splitlines()
            pairs.append([literal_eval(pair_lst[0]), literal_eval(pair_lst[1])])
        return pairs

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        indices = []

        def cmp(a: Union[list, int], b: Union[list, int]) -> int:
            match (isinstance(a, int), isinstance(b, int)):
                case True, True:
                    if a == b:
                        return 0
                    if a < b:
                        return -1
                    return 1
                case True, False:
                    return cmp([a], b)
                case False, True:
                    return cmp(a, [b])
                case False, False:
                    match (a, b):
                        case ([x, *_], [y, *_]):
                            match cmp(x, y):
                                case -1:
                                    return -1
                                case 0:
                                    return cmp(a[1:], b[1:])
                                case 1:
                                    return 1
                        case ([], [y, *_]):
                            return -1
                        case ([], []):
                            return 0
                        case ([x, *_], []):
                            return 1

        for i, pair in enumerate(parsed_data):
            left, right = pair
            if cmp(left, right) == -1:
                indices.append(i + 1)
        return sum(indices)

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        packets = [item for sublist in parsed_data for item in sublist]

        a = [[2]]
        b = [[6]]

        def cmp(a: Union[list, int], b: Union[list, int]) -> int:
            match (isinstance(a, int), isinstance(b, int)):
                case True, True:
                    if a == b:
                        return 0
                    if a < b:
                        return -1
                    return 1
                case True, False:
                    return cmp([a], b)
                case False, True:
                    return cmp(a, [b])
                case False, False:
                    match (a, b):
                        case ([x, *_], [y, *_]):
                            match cmp(x, y):
                                case -1:
                                    return -1
                                case 0:
                                    return cmp(a[1:], b[1:])
                                case 1:
                                    return 1
                        case ([], [y, *_]):
                            return -1
                        case ([], []):
                            return 0
                        case ([x, *_], []):
                            return 1

        packets.extend([a, b])
        packets.sort(key=cmp_to_key(cmp))
        return (packets.index(a) + 1) * (packets.index(b) + 1)
