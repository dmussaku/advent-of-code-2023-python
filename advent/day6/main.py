from functools import reduce
from typing import List, Tuple


def parse_times_and_distances_part1(file_path) -> List[Tuple[int, int]]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    times = [
        int(line.strip())
        for line in filter(
            lambda x: x != "", lines[0].strip("Time:").strip("\n").split(" ")
        )
    ]
    distances = [
        int(line.strip())
        for line in filter(
            lambda x: x != "", lines[1].strip("Distances:").strip("\n").split(" ")
        )
    ]
    return list(zip(times, distances))


def parse_times_and_distances_part2(file_path) -> Tuple[int, int]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    time = int(lines[0].strip("Time:").strip("\n").replace(" ", ""))
    distance = int(lines[1].strip("Distance:").strip("\n").replace(" ", ""))

    return (time, distance)


def distance_traveled(button_held_time: int, max_time: int):
    return button_held_time * (max_time - button_held_time)


def winning_possibilities(max_time: int, win_distance: int):
    results = [
        (button_held_time, distance_traveled(button_held_time, max_time))
        for button_held_time in range(max_time)
        if distance_traveled(button_held_time, max_time) > win_distance
    ]
    return results


def run_part_1(file_path):
    times_and_distances = parse_times_and_distances_part1(file_path)
    results = []
    for max_time, max_distance in times_and_distances:
        results.append(len(winning_possibilities(max_time, max_distance)))

    return reduce(lambda x, y: x * y, results)


def run_part_2(file_path):
    time, distance = parse_times_and_distances_part2(file_path)
    result = len(winning_possibilities(time, distance))
    return result
