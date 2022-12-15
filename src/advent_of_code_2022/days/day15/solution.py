"""
"""
import re
import sys

from advent_of_code_2022.utils import AoCData, Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 15, year: int = 2022) -> None:
        super().__init__(day, year)

    def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
        """ """
        sensor_string_list = input_data.splitlines()
        sensors_beacons = []
        for sensor_string in sensor_string_list:
            sens_x, sens_y, beac_x, beac_y = re.findall(r"-?\d+", sensor_string)
            sensors_beacons.append(
                [[int(sens_x), int(sens_y)], [int(beac_x), int(beac_y)]]
            )
        return sensors_beacons

    def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        no_beacon_pos = set()
        beacons_in_row = set()
        row_to_check = 2000000
        if "pytest" in sys.modules:
            row_to_check = 10
        for sen_bea in parsed_data:
            if sen_bea[1][1] == row_to_check:
                beacons_in_row.add((sen_bea[1][0], sen_bea[1][1]))
            dist = abs(sen_bea[0][0] - sen_bea[1][0]) + abs(
                sen_bea[0][1] - sen_bea[1][1]
            )
            if abs(sen_bea[0][1] - row_to_check) >= dist:
                continue
            else:
                overlap = dist - abs(sen_bea[0][1] - row_to_check)
                no_beacon_pos.update(
                    list(range(sen_bea[0][0] - overlap, sen_bea[0][0] + overlap + 1))
                )
        return len(no_beacon_pos) - len(beacons_in_row)

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        for row in range(4_000_001):
            no_beacon_pos = set()
            beacons_in_row = set()
            for sen_bea in parsed_data:
                if sen_bea[1][1] == row:
                    beacons_in_row.add((sen_bea[1][0], sen_bea[1][1]))
                dist = abs(sen_bea[0][0] - sen_bea[1][0]) + abs(
                    sen_bea[0][1] - sen_bea[1][1]
                )
                if abs(sen_bea[0][1] - row) >= dist:
                    continue
                else:
                    overlap = dist - abs(sen_bea[0][1] - row)
                    no_beacon_pos.update(
                        list(
                            range(
                                max(0, sen_bea[0][0] - overlap),
                                min(4_000_000, sen_bea[0][0] + overlap + 1),
                            )
                        )
                    )
            if row % 100 == 0:
                print(row)
                print(len(no_beacon_pos))
            if len(no_beacon_pos) == 3_999_999:
                return (
                    4_000_000 * no_beacon_pos.difference(list(range(4_000_001))) + row
                )
