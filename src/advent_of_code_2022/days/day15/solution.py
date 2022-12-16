"""
"""
import itertools
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

    def _rotate_boxes(
        self: "DaySolution", parsed_data: AoCData
    ) -> list[list[list[list[int]]]]:
        # First rotate all sensors 45 degrees to obtain square search spaces
        boxes = []
        for sen_bea in parsed_data:
            sen, bea = sen_bea
            dist = abs(sen[0] - bea[0]) + abs(sen[1] - bea[1])
            corners = [
                [sen[0] + dist, sen[1]],
                [sen[0], sen[1] - dist],
                [sen[0] - dist, sen[1]],
                [sen[0], sen[1] + dist],
            ]
            rot_corners = [
                [corners[0][0] - corners[0][1], corners[0][0] + corners[0][1]],
                [corners[1][0] - corners[1][1], corners[1][0] + corners[1][1]],
                [corners[2][0] - corners[2][1], corners[2][0] + corners[2][1]],
                [corners[3][0] - corners[3][1], corners[3][0] + corners[3][1]],
            ]
            boxes.append(rot_corners)
        return boxes

    def _get_space_coords(
        self: "DaySolution", boxes: list[list[list[list[int]]]]
    ) -> tuple(set[int], set[int]):
        # First find all columns that are exactly between two boxes
        xs = set()
        for box1, box2 in itertools.combinations(boxes, 2):
            if abs(box1[2][0] - box2[1][0]) == 2:
                xs.add(box1[2][0] - 1)
            elif abs(box2[2][0] - box1[1][0]) == 2:
                xs.add(box2[2][0] - 1)

        ys = set()
        for box1, box2 in itertools.combinations(boxes, 2):
            if abs(box1[3][1] - box2[1][1]) == 2:
                ys.add(box1[3][1] + 1)
            elif abs(box2[3][1] - box1[1][1]) == 2:
                ys.add(box2[3][1] + 1)
        return xs, ys

    def _check_box_coverage(
        self: "DaySolution", x: int, y: int, boxes: list[list[list[list[int]]]]
    ) -> list[int]:
        cov_sides = [0, 0, 0, 0]
        for box in boxes:
            if box[0][0] == x - 1 and (box[1][1] <= y <= box[0][1]):
                cov_sides[0] = 1
                continue
            elif box[2][0] == x + 1 and (box[1][1] <= y <= box[0][1]):
                cov_sides[1] = 1
                continue
            elif box[0][1] == y - 1 and (box[2][0] <= x <= box[1][0]):
                cov_sides[2] = 1
                continue
            elif box[2][1] == y + 1 and (box[2][0] <= x <= box[1][0]):
                cov_sides[3] = 1
                continue
        return cov_sides

    def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
        """ """
        if "pytest" in sys.modules:
            search_range = 20
        else:
            search_range = 4_000_000

        boxes = self._rotate_boxes(parsed_data)
        xs, ys = self._get_space_coords(boxes)

        for y in ys:
            if 0 <= y <= 2 * search_range:
                for x in xs:
                    if -search_range <= x <= search_range:
                        cov_sides = self._check_box_coverage(x, y, boxes)
                        if sum(cov_sides) == 4:  # Found our point
                            rot_x = (x + y) // 2
                            rot_y = (y - x) // 2
                            return 4000000 * rot_x + rot_y
        return 1
