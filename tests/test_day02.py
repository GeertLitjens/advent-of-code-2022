import pytest

from advent_of_code_2022.days.day02.solution import DaySolution


@pytest.fixture
def day_testdata() -> str:
    return """\
A Y
B X
C Z\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == 15


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == 12
