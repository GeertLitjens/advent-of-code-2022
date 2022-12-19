"""
"""

import re
from collections import defaultdict

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 16, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        valve_flow_rate = {}
        dist_matrix = defaultdict(1000)
        valve_string = input_data.splitlines()
        for v_str in valve_string:
            match_dct = re.match(
                r"Valve (?P<name>..) has flow rate=(?P<flow_rate>\d+); "
                r"tunnels lead to valves (?P<nbs>.*)",
                v_str,
            )
            if int_flow_rate := int(match_dct["flow_rate"]) > 0:
                valve_flow_rate[match_dct["flow_rate"]] = int_flow_rate
            for nb in match_dct["nbs"].split(", "):
                dist_matrix[match_dct["flow_rate"] + "," + nb] = 1

        return valve_flow_rate, dist_matrix

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        return 1

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        return 1
