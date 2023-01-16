import pytest

from advent_of_code_2022.days.day19.solution import DaySolution


@pytest.fixture
def day_testdata() -> str:
    return """\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore.\
Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore.\
Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == 33


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == 56 * 62
