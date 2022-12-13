"""
It is slowly starting to get a bit more challenging. although this was also mainly an exercise
requiring good bookkeeping, and less conceptual knowledge. In the end you need to update all
the parents of the subfolders to track the size.
"""
from collections import defaultdict
from pathlib import PurePath

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 7, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """
        Simply pass the instructions as a list of lines.
        """
        return input_data.splitlines()

    def _traverse_filesystem(
        self: "DaySolution", instructions: list[str]
    ) -> dict[str, int]:
        """
        The actual traversal. Maybe it could be done with nicer loops, but I guess it is ok.
        """
        cur_path = PurePath("/")
        path_to_size = defaultdict(lambda: 0)
        i = 0
        while i < len(instructions):
            instruction = instructions[i]
            if instruction[:5] == "$ cd ":
                if instruction[5:] == "..":
                    cur_path = cur_path.parent
                else:
                    cur_path = cur_path / instruction[5:]
            elif instruction[:5] == "$ ls":
                j = i + 1
                while j < len(instructions):
                    ls_out = instructions[j]
                    if "$" == ls_out[0]:
                        break
                    if "dir" not in ls_out:
                        path_to_size[str(cur_path)] += int(ls_out.split(" ")[0])
                        parent_path = cur_path
                        while str(parent_path) != "/":
                            parent_path = parent_path.parent
                            path_to_size[str(parent_path)] += int(ls_out.split(" ")[0])
                    j += 1
                i = j - 1
            i += 1
        return path_to_size

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        I use the PurePatch class from the pathlib library to prevent using
        any actual OS operations. Just keep tracking the current path and
        whenever encountering a file, update the size of the parents which are
        stored in a dictionary. Then return the total bytes of all folders
        below 100000.
        """
        path_to_size = self._traverse_filesystem(parsed_data)
        total_bytes = sum([x for x in path_to_size.values() if x <= 100000])
        return total_bytes

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """
        Same, but now calculate the total space to free, iterate over the paths
        and return the size of the path that leads to the minimal removal.
        """
        path_to_size = self._traverse_filesystem(parsed_data)
        bytes_to_free = 30000000 - (70000000 - path_to_size["/"])
        for path_and_size in sorted(path_to_size.items(), key=lambda x: x[1]):
            if path_and_size[1] >= bytes_to_free:
                return path_and_size[1]
        return 0
