"""
"""

from advent_of_code_2022.utils import AoCData, Solution


class Elem:
    def __init__(
        self: "Elem", value: int, prev: "Elem" = None, next: "Elem" = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self: "Elem") -> str:
        return str(self.value)

    def __add__(self: "Elem", nr: int) -> "Elem":
        elem = self
        for _ in range(nr):
            elem = elem.next
        return elem


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 20, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        link_list = [Elem(int(x)) for x in input_data.splitlines()]
        for el_i, el in enumerate(link_list[:-1]):
            link_list[el_i - 1].next = el
            link_list[el_i + 1].prev = el
        link_list[0].prev = link_list[-1]
        link_list[-2].next = link_list[-1]
        return link_list

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for el in parsed_data:
            move = el.value % (len(parsed_data) - 1)
            if move != 0:
                new_prev = el + move
                el.next.prev = el.prev
                el.prev.next = el.next
                el.next = new_prev.next
                new_prev.next.prev = el
                new_prev.next = el
                el.prev = new_prev

        result = 0
        for el in parsed_data:
            if el.value == 0:
                cur_el = el
                for el_i in range(1, 3001):
                    cur_el = cur_el.next
                    if el_i % 1000 == 0:
                        result += cur_el.value
        return result

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for el in parsed_data:
            el.value *= 811589153

        for _ in range(10):
            for el in parsed_data:
                move = el.value % (len(parsed_data) - 1)
                if move != 0:
                    new_prev = el + move
                    el.next.prev = el.prev
                    el.prev.next = el.next
                    el.next = new_prev.next
                    new_prev.next.prev = el
                    new_prev.next = el
                    el.prev = new_prev

        result = 0
        for el in parsed_data:
            if el.value == 0:
                cur_el = el
                for el_i in range(1, 3001):
                    cur_el = cur_el.next
                    if el_i % 1000 == 0:
                        result += cur_el.value
        return result
