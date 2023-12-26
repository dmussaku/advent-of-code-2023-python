import pytest

from .main import run_part_1, run_part_2, parse_file, source_destination_map, find_range_overlaps


def test_parse_file():
    result = parse_file('day5/input/test_file.txt')
    assert result == {'seeds': [79, 14, 55, 13],
                    'seed-to-soil map': [[50, 98, 2], [52, 50, 48]],
                    'soil-to-fertilizer map': [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
                    'fertilizer-to-water map': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
                    'water-to-light map': [[88, 18, 7], [18, 25, 70]],
                    'light-to-temperature map': [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
                    'temperature-to-humidity map': [[0, 69, 1], [1, 0, 69]],
                    'humidity-to-location map': [[60, 56, 37], [56, 93, 4]]}

@pytest.mark.parametrize('val,input_ranges,expected', (
    (0, [[50, 98, 2], [52, 50, 48]], 0),
    (49, [[50, 98, 2], [52, 50, 48]], 49),
    (50, [[50, 98, 2], [52, 50, 48]], 52),
    (79, [[50, 98, 2], [52, 50, 48]], 81),
    (96, [[50, 98, 2], [52, 50, 48]], 98),
    (99, [[50, 98, 2], [52, 50, 48]], 51),
    (0, [[50, 98, 2], [52, 50, 48]], 0),
    (10, [[50, 98, 2], [52, 50, 48]], 10),
    (53, [[50, 98, 2], [52, 50, 48]], 55),
    (81, [[0,15,37], [37,52,2], [39,0,15]], 81),
    (14, [[0,15,37], [37,52,2], [39,0,15]], 53),
))
def test_source_destination_map(val, input_ranges, expected):
    assert source_destination_map(val, input_ranges) == expected




@pytest.mark.parametrize('init_range,compared_range,expected', (
    (range(5, 10), range(1,2), [range(5, 10)]),
    (range(5, 10), range(4,6), [range(5, 6), range(6, 10)]),
    (range(5, 10), range(6,8), [range(5, 6), range(6, 8), range(8, 10)]),
    (range(5, 10), range(8,11), [range(5, 8), range(8, 10)]),
    (range(5, 10), range(13, 18), [range(5, 10)]),
))
def test_find_range_overlaps(init_range, compared_range, expected):
    assert find_range_overlaps(init_range, compared_range) == expected
    


def test_run_part_1():
    assert run_part_1('day5/input/test_file.txt') == 35


def test_run_part_2():
    assert run_part_2('day5/input/test_file.txt') == 46