"""
"""
from collections import defaultdict
from pathlib import PurePath

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 7, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        return input_data.splitlines()

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        cur_path = PurePath("/")
        path_to_size = defaultdict(lambda: 0)
        i = 0
        while i < len(parsed_data):
            instruction = parsed_data[i]
            if instruction[:5] == "$ cd ":
                if instruction[5:] == "..":
                    cur_path = cur_path.parent
                else:
                    cur_path = cur_path / instruction[5:]
            elif instruction[:5] == "$ ls":
                j = i + 1
                ls_out = parsed_data[j]
                while ls_out[0] != "$":
                    if "dir" not in ls_out:
                        parent_path = cur_path
                        while str(parent_path) != "/":
                            path_to_size[str(parent_path)] += int(ls_out.split(" ")[0])
                            parent_path = parent_path.parent
                    j += 1
                    if j >= len(parsed_data):
                        break
                    ls_out = parsed_data[j]
                i = j - 1
            i += 1
        total_bytes = sum([x for x in path_to_size.values() if x <= 100000])
        return total_bytes

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        cur_path = PurePath("/")
        path_to_size = defaultdict(lambda: 0)
        i = 0
        while i < len(parsed_data):
            instruction = parsed_data[i]
            if instruction[:5] == "$ cd ":
                if instruction[5:] == "..":
                    cur_path = cur_path.parent
                else:
                    cur_path = cur_path / instruction[5:]
            elif instruction[:5] == "$ ls":
                j = i + 1
                ls_out = parsed_data[j]
                while ls_out[0] != "$":
                    if "dir" not in ls_out:
                        parent_path = cur_path
                        while str(parent_path) != "/":
                            path_to_size[str(parent_path)] += int(ls_out.split(" ")[0])
                            parent_path = parent_path.parent
                        path_to_size[str(parent_path)] += int(ls_out.split(" ")[0])
                    j += 1
                    if j >= len(parsed_data):
                        break
                    ls_out = parsed_data[j]
                i = j - 1
            i += 1
        #        bytes_to_free = 30000000 - (70000000 - path_to_size["/"])
        #        for path_and_size in sorted(path_to_size.items(), key=lambda x: x[1]):
        #            if path_and_size[1] >= bytes_to_free:
        #                return path_and_size[1]
        return 0
