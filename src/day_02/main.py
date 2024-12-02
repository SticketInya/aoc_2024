from typing import List
import re


def main() -> None:
    print("Advent of code 2024 - Day 02")

    f = open("./src/day_02/input.txt", "r")

    reports: List[List[int]] = []
    for line in f:
        nums = re.findall(r"\d+", line)
        report = []
        for num in nums:
            report.append(int(num))
        reports.append(report)

    print(f"part1: {count_safe_reports(reports)}")
    print(f"part1: {count_safe_reports(reports, tolerance=1)}")


def count_safe_reports(
    reports: List[List[int]], min_diff=1, max_diff=3, tolerance=0
) -> int:
    total_safe_reports: int = 0
    for report in reports:

        def check_report(report: List[int]) -> bool:
            tolerance_left = tolerance
            direction: int = 0
            previous = report[0]
            for el in report[1:]:
                diff = previous - el

                if direction == 0:
                    direction = diff
                else:
                    if direction < 0 and diff > 0 or direction > 0 and diff < 0:
                        if tolerance_left > 0:
                            tolerance_left -= 1
                            continue
                        # print(f"{report} invalid direction at {i}")
                        return False

                diff = abs(diff)
                if diff < min_diff or diff > max_diff:
                    if tolerance_left > 0:
                        tolerance_left -= 1
                        continue
                    # print(f"{report} invalid difference {diff} at {i}")
                    return False
                previous = el
            return True

        reversed_copy = report.copy()
        reversed_copy.reverse()

        if check_report(report) or check_report(reversed_copy):
            # print(f"{report} is safe")
            total_safe_reports += 1

    return total_safe_reports


if __name__ == "__main__":
    main()
