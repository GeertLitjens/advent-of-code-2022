"""
"""
import math

from advent_of_code_2022.utils import AoCData, Solution


def parse_eq(eq: dict[str], monkeys: dict[str], humn: int) -> int:
    lh, rh = None, None
    if isinstance(monkeys[eq["lh"]], dict):
        lh = parse_eq(monkeys[eq["lh"]], monkeys, humn)
    else:
        lh = monkeys[eq["lh"]] if eq["lh"] != "humn" else humn
    if isinstance(monkeys[eq["rh"]], dict):
        rh = parse_eq(monkeys[eq["rh"]], monkeys, humn)
    else:
        rh = monkeys[eq["rh"]] if eq["rh"] != "humn" else humn
    result = 0
    if eq["op"] == "+":
        result = lh + rh
    elif eq["op"] == "-":
        result = lh - rh
    elif eq["op"] == "*":
        result = lh * rh
    elif eq["op"] == "/":
        result = lh // rh
    return result


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 21, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        monkeys = {}
        for line in input_data.splitlines():
            name, eq = line.split(": ")
            if eq.isdigit():
                monkeys[name] = int(eq)
            else:
                lh, op, rh = eq.split(" ")
                monkeys[name] = {"lh": lh, "op": op, "rh": rh}
        return monkeys

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        return parse_eq(parsed_data["root"], parsed_data, parsed_data["humn"])

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        parsed_data["root"]["op"] = "-"
        bot, top = 0, 1e16
        res = 1
        while top != bot:
            res = parse_eq(parsed_data["root"], parsed_data, ((bot + top) // 2))
            if res > 0:
                bot = math.ceil((bot + top) / 2)
            else:
                top = math.floor((bot + top) / 2)
        res = parse_eq(parsed_data["root"], parsed_data, ((bot + top) // 2))
        if res == 0:
            return (bot + top) // 2
        bot, top = 0, 1e16
        res = 1
        while top != bot:
            res = parse_eq(parsed_data["root"], parsed_data, ((bot + top) // 2))
            if res < 0:
                bot = math.ceil((bot + top) / 2)
            else:
                top = math.floor((bot + top) / 2)
        res = parse_eq(parsed_data["root"], parsed_data, ((bot + top) // 2))
        return (bot + top) // 2
