"""
"""

import functools
import itertools
import re
from collections import defaultdict

from frozendict import frozendict

from advent_of_code_2022.utils import AoCData, Solution


@functools.cache
def score(
    valve_flow_rate: dict[int],
    dist_matrix: defaultdict[int],
    unopened_valves: set[str],
    time_left: int,
    cur_location: str,
    cur_flow_rate: int,
    elephant: bool = False,
) -> int:
    valve_score = 0
    if cur_flow_rate > 0 and time_left > 0:
        time_left -= 1
        valve_score = time_left * cur_flow_rate
    rem_valve_scores = [0]
    elph_scores = [0]
    for valve in unopened_valves:
        rem_valves = unopened_valves - {valve}
        cur_flow_rate = valve_flow_rate[valve]
        if time_left > 0:
            rem_valve_scores.append(
                score(
                    valve_flow_rate,
                    dist_matrix,
                    rem_valves,
                    time_left - dist_matrix[cur_location, valve],
                    valve,
                    cur_flow_rate,
                    elephant,
                )
            )
        if elephant:
            elph_scores.append(
                score(
                    valve_flow_rate,
                    dist_matrix,
                    unopened_valves,
                    26,
                    "AA",
                    0,
                )
            )
    return valve_score + max(rem_valve_scores + elph_scores)


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 16, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        valve_string = input_data.splitlines()
        valves = set()
        dist_matrix = defaultdict(lambda: 1000)
        valve_flow_rate = {}
        for v_str in valve_string:
            match_dct = re.match(
                r"Valve (?P<name>..) has flow rate=(?P<flow_rate>\d+); "
                r"tunnels{0,1} leads{0,1} to valves{0,1} (?P<nbs>.*)",
                v_str,
            )
            valves.add(match_dct["name"])
            if (int_flow_rate := int(match_dct["flow_rate"])) > 0:
                valve_flow_rate[match_dct["name"]] = int_flow_rate
            for nb in match_dct["nbs"].split(", "):
                dist_matrix[match_dct["name"], nb] = 1

        for k, i, j in itertools.product(valves, valves, valves):  # floyd-warshall
            dist_matrix[i, j] = min(
                dist_matrix[i, j],
                dist_matrix[i, k] + dist_matrix[k, j],
            )

        return valve_flow_rate, dist_matrix

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        valve_flow_rate, dist_matrix = parsed_data
        return score(
            frozendict(valve_flow_rate),
            frozendict(dist_matrix),
            frozenset(valve_flow_rate),
            30,
            "AA",
            0,
        )

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        valve_flow_rate, dist_matrix = parsed_data
        return score(
            frozendict(valve_flow_rate),
            frozendict(dist_matrix),
            frozenset(valve_flow_rate),
            26,
            "AA",
            0,
            True,
        )
