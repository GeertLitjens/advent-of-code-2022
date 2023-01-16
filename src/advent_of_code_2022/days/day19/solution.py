"""
"""

import re
from math import ceil

from advent_of_code_2022.utils import AoCData, Solution


class State:
    def __init__(self: "State", resources: list[int], robots: list[int]) -> None:
        self.resources = resources
        self.robots = robots

    def __hash__(self: "State") -> int:
        return hash(tuple(self.resources + self.robots))

    def copy(self: "State") -> "State":
        return State(list(self.resources), list(self.robots))


def get_options(state: State, blueprint: tuple[tuple[int]]) -> dict[str]:
    options = {}
    if state.robots[0] < blueprint[4][0]:
        options["ore"] = (
            0
            if state.resources[0] >= blueprint[0][0]
            else ceil((blueprint[0][0] - state.resources[0]) / state.robots[0])
        )
    if state.robots[1] < blueprint[4][1]:
        options["clay"] = (
            0
            if state.resources[0] >= blueprint[1][0]
            else ceil((blueprint[1][0] - state.resources[0]) / state.robots[0])
        )
    if state.robots[1] > 0 and state.robots[2] < blueprint[4][2]:
        options["obsidian"] = (
            0
            if state.resources[0] >= blueprint[2][0]
            and state.resources[1] >= blueprint[2][1]
            else max(
                [
                    ceil((blueprint[2][0] - state.resources[0]) / state.robots[0]),
                    ceil((blueprint[2][1] - state.resources[1]) / state.robots[1]),
                ]
            )
        )
    if state.robots[2] > 0:
        options["geode"] = (
            0
            if state.resources[0] >= blueprint[3][0]
            and state.resources[2] >= blueprint[3][2]
            else max(
                [
                    ceil((blueprint[3][0] - state.resources[0]) / state.robots[0]),
                    ceil((blueprint[3][2] - state.resources[2]) / state.robots[2]),
                ]
            )
        )
    return options


def pursue_options(
    state: State,
    blueprint: tuple[tuple[int]],
    time_left: int,
    cur_max: int,
    options: dict[str],
) -> int:
    for option in options:
        new_state = state.copy()
        if option == "ore":
            dt = min(time_left - 1, options["ore"])
            for _ in range(dt):
                new_state.resources = [
                    x + y for x, y in zip(new_state.robots, new_state.resources)
                ]
            new_state.resources[0] -= blueprint[0][0]
            new_state.robots[0] += 1
            cur_max = max(
                simulate(new_state.copy(), blueprint, time_left - dt - 1, cur_max),
                cur_max,
            )
        elif option == "clay":
            dt = min(time_left - 1, options["clay"])
            for _ in range(dt):
                new_state.resources = [
                    x + y for x, y in zip(new_state.robots, new_state.resources)
                ]
            new_state.resources[0] -= blueprint[1][0]
            new_state.robots[1] += 1
            cur_max = max(
                simulate(new_state.copy(), blueprint, time_left - dt - 1, cur_max),
                cur_max,
            )
        elif option == "obsidian":
            dt = min(time_left - 1, options["obsidian"])
            for _ in range(dt):
                new_state.resources = [
                    x + y for x, y in zip(new_state.robots, new_state.resources)
                ]
            new_state.resources[0] -= blueprint[2][0]
            new_state.resources[1] -= blueprint[2][1]
            new_state.robots[2] += 1
            cur_max = max(
                simulate(new_state.copy(), blueprint, time_left - dt - 1, cur_max),
                cur_max,
            )
        elif option == "geode":
            dt = min(time_left - 1, options["geode"])
            for _ in range(dt):
                new_state.resources = [
                    x + y for x, y in zip(new_state.robots, new_state.resources)
                ]
            new_state.resources[0] -= blueprint[3][0]
            new_state.resources[2] -= blueprint[3][2]
            new_state.robots[3] += 1
            cur_max = max(
                simulate(new_state.copy(), blueprint, time_left - dt - 1, cur_max),
                cur_max,
            )
    return cur_max


def simulate(
    state: State, blueprint: tuple[tuple[int]], time_left: int, cur_max: int
) -> int:
    pos_max = (
        state.resources[3]
        + state.robots[3] * time_left
        + (time_left * (time_left - 1) / 2)
    )
    if pos_max <= cur_max:
        return cur_max
    if time_left < 1:
        return state.resources[3]

    options = get_options(state, blueprint)

    state.resources = [x + y for x, y in zip(state.robots, state.resources)]

    return pursue_options(state, blueprint, time_left, cur_max, options)


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 19, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        blueprints = []
        for bp in input_data.splitlines():
            costs = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            blueprint_ints = [int(x) for x in re.findall(r"\d+", bp)][1:]
            costs[0][0] = blueprint_ints[0]
            costs[1][0] = blueprint_ints[1]
            costs[2][0] = blueprint_ints[2]
            costs[2][1] = blueprint_ints[3]
            costs[3][0] = blueprint_ints[4]
            costs[3][2] = blueprint_ints[5]
            costs[4][0] = max([costs[0][0], costs[1][0], costs[2][0], costs[3][0]])
            costs[4][1] = max([costs[0][1], costs[1][1], costs[2][1], costs[3][1]])
            costs[4][2] = max([costs[0][2], costs[1][2], costs[2][2], costs[3][2]])
            costs = tuple(tuple(x) for x in costs)
            blueprints.append(costs)
        return blueprints

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        qls = 0
        for bp_id, bp in enumerate(parsed_data):
            state = State([0, 0, 0, 0], [1, 0, 0, 0])
            max_geodes = simulate(state, bp, 24, 0)
            qls += max_geodes * (bp_id + 1)
        return qls

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        qls = 1
        for bp in parsed_data[:3]:
            state = State([0, 0, 0, 0], [1, 0, 0, 0])
            max_geodes = simulate(state, bp, 32, 0)
            qls *= max_geodes
        return qls
