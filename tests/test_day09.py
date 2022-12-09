import pytest

from advent_of_code_2022.days.day09.solution import DaySolution


@pytest.fixture
def day_testdata() -> str:
    return """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == 88


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == 36
