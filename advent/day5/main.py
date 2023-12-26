from typing import Dict, List, Union


def parse_file(file_path) -> Dict[str, List[Union[List[int], int]]]:
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    result :Dict[str, List[int]] = {}
    current_key = None
    for line in filter(lambda x: x not in ('', '\n'), lines):
        if line.startswith('seeds:'):
            rest = line.split(':')[-1]
            result['seeds'] = [int(val) for val in filter(lambda x: x!= '', rest.strip('\n').split(' '))]
        elif ':' in line:
            current_key, rest = line.split(':')
            result[current_key] = []
        else:
            result[current_key].append([int(val) for val in filter(lambda x: x!= '', line.strip('\n').split(' '))])
    return result


def source_destination_map(number: int, destination_source_ranges: List[List[int]]):
    for destination, source, range_len in destination_source_ranges:
        if number >= source and number < source + range_len:
            return (number - source) + destination
    return number


def find_range_overlap(range1: range, range2: range) -> range:
    if range1.start > range2.start:
        range1, range2 = range2, range1
    if range1.stop < range2.start:
        return None
    return range(range2.start, min(range1.stop, range2.stop))


def source_destination_range_map(number_range: range, destination_source_ranges: List[List[int]]) -> List[range]:
    resulting_ranges = []
    
    # first we need to divide the ranges into different ranges on intersections
    for destination, source, range_len in destination_source_ranges:
        r = range(source, source + range_len)
        intersection = find_range_overlap(number_range, r)
        if not intersection:
            continue


def run_part_1(input):
    input_map = parse_file(input)
    seeds = input_map.pop('seeds')
    results = []
    for seed in seeds:
        current_position = seed
        for key, destination_source_ranges in input_map.items():
            current_position = source_destination_map(current_position, destination_source_ranges)
        results.append(current_position)
    return min(results)


def run_part_2(input):
    input_map = parse_file(input)
    seeds = input_map.pop('seeds')
    seed_pairs = [(seeds[i], seeds[i+1])for i in range(0, len(seeds)-1, 2)]
    results = []
    for seed_pair in seed_pairs:
        print(seed_pair)
        for seed in range(seed_pair[0], seed_pair[0]+seed_pair[1] - 1):
            current_position = seed
            for key, destination_source_ranges in input_map.items():
                current_position = source_destination_map(current_position, destination_source_ranges)
            results.append(current_position)
    return min(results)


