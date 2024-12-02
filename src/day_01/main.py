from typing import List
import re


def main() -> None:
    print("Advent of code 2024 - Day 01")

    f = open("./src/day_01/input.txt", "r")

    l1: List[int] = []
    l2: List[int] = []
    for line in f:
        nums = re.findall(r"\d+", line)
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))

    print(f"part1: {calc_distance_between_lists(l1,l2)}")
    print(f"part2: {calc_similarity_score(l1,l2)}")


def calc_distance_between_lists(l1: List[int], l2: List[int]) -> int:
    l1.sort()
    l2.sort()

    total_distance = 0
    for i, el in enumerate(l1):
        total_distance += el - l2[i] if el > l2[i] else l2[i] - el

    return total_distance


def calc_similarity_score(l1: List[int], l2: List[int]) -> int:

    total_similarity = 0
    for el in l1:
        count = l2.count(el)
        total_similarity += el * count
    return total_similarity


if __name__ == "__main__":
    main()
