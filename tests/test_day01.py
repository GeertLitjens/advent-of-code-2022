import pytest

from advent_of_code_2022.days.day01.solution import DaySolution


@pytest.fixture
def day_testdata() -> str:
    return """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
"""


def test_part1(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part1(parsed_data)
    assert result == 24000


def test_part2(day_testdata: str) -> None:
    sol = DaySolution()
    parsed_data = sol._parse_data(day_testdata)
    result = sol._solve_part2(parsed_data)
    assert result == 45000
