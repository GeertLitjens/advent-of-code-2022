"""
"""
import ast
from dataclasses import dataclass
from math import prod

from advent_of_code_2022.utils import AoCData, Solution


@dataclass
class Monkey:
    items: list[int]
    operation: str
    buddies: tuple[int]
    divisor: int
    items_inspected: int = 0
    reduce_worry: int = 0

    def inspect_all_items(self: "Monkey", monkeys: list["Monkey"]) -> None:
        while self.items:
            item = self.items.pop(0)
            item = self._apply_operation(item)
            if self.reduce_worry == 0:
                item = item // 3
            else:
                item = item % self.reduce_worry
            if item % self.divisor == 0:
                monkeys[self.buddies[0]].items.append(item)
            else:
                monkeys[self.buddies[1]].items.append(item)
            self.items_inspected += 1

    def _apply_operation(self: "Monkey", old: int) -> int:
        return int(ast.literal_eval(self.operation))


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 11, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        monkey_strings = input_data.split("\n\n")
        monkeys = []
        for monkey_string in monkey_strings:
            monkey_lines = monkey_string.splitlines()
            items = [
                int(x) for x in monkey_lines[1].split("Starting items: ")[1].split(", ")
            ]
            operation = monkey_lines[2].split("Operation: ")[1].split("new = ")[1]
            divisor = int(monkey_lines[3].split("Test: divisible by ")[1])
            buddy_1 = int(monkey_lines[4].split("If true: throw to monkey ")[1])
            buddy_2 = int(monkey_lines[5].split("If false: throw to monkey ")[1])
            monkeys.append(Monkey(items, operation, (buddy_1, buddy_2), divisor))

        return monkeys

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for _ in range(20):
            for monkey in parsed_data:
                monkey.inspect_all_items(parsed_data)
        inspections = sorted([m.items_inspected for m in parsed_data], reverse=True)
        return inspections[0] * inspections[1]

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for monkey in parsed_data:
            monkey.reduce_worry = prod([x.divisor for x in parsed_data])
        for _ in range(10000):
            for monkey in parsed_data:
                monkey.inspect_all_items(parsed_data)
        inspections = sorted([m.items_inspected for m in parsed_data], reverse=True)
        return inspections[0] * inspections[1]
