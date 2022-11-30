# This script runs the solutions for all days of the Advent of Code 2021
import argparse
import importlib
import logging
import os
from pathlib import Path

from utils import ColorLogger


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run (a subset of) the solutions for the Advent of Code 2022 \
                     or create the entries for a new day"
    )
    parser.add_argument(
        "token",
        type=str,
        default="",
        help="Advent of Code session token to access your user's progress",
    )
    parser.add_argument(
        "-d",
        "--days",
        type=int,
        metavar="N",
        nargs="*",
        default=[],
        help="Run a specific set of days, default is all days. If you want to run \
              a specific part of a day, specify an a or a b after the day number \
              (e.g. 11a, 12b)",
    )
    parser.add_argument(
        "-s",
        "--submit",
        action="store_true",
        help="Submit answers to Advent of Code website",
    )
    parser.add_argument(
        "-b",
        "--blog",
        action="store_true",
        help="Generate MD files for GitHub pages from code",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase verbosity for debug purposes",
    )
    args = parser.parse_args()

    logging.setLoggerClass(ColorLogger)
    logger = logging.getLogger("aoclogger")
    if args.verbose:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    if args.token:
        os.environ["AOC_TOKEN"] = args.token
    elif os.path.exists(".aoc_token"):
        os.environ["AOC_TOKEN"] = Path(".aoc_token").read_text()

    day_folders = [x for x in os.listdir(os.getcwd()) if "day" in x]
    if args.days:
        days = args.days
    else:
        days = sorted([int(x.replace("day", "")) for x in day_folders])

    logger.info("Started calculating solutions for days: " + str(days))
    for day_nr in days:
        day_module = importlib.import_module("day" + str(day_nr) + ".solution")
        solution = day_module.DaySolution()
        solution.solve(args.part1)
        if args.submit:
            solution.submit()
        if args.write:
            solution.generate_day_md()
