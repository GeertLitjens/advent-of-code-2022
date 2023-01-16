import pytest

from advent_of_code_2022.days.day20.solution import DaySolution


@pytest.fixture
def day_testdata() -> str:
    return """\
1
2
-3
3
-2
0
4\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == 3


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == 1623178306
