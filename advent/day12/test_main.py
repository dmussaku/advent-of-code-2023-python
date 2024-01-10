import pytest

from .main import run_part_1, run_part_2, parse_input, get_all_combinations, get_valid_combinations, form_a_valid_regex


def test_parse_input():
    assert parse_input('day12/input/test_file.txt') == [("???.###", [1,1,3]),
    (".??..??...?##.", [1,1,3]),
    ("?#?#?#?#?#?#?#?", [1,3,1,6]),
    ("????.#...#...", [4,1,1]),
    ("????.######..#####.", [1,6,5]),
    ("?###????????", [3,2,1]),]

@pytest.mark.parametrize("line,expected", (
    ('?.?', ['...', '#..', '..#', '#.#']),
))
def test_get_all_combinations(line, expected):
    assert sorted(list(get_all_combinations(line))) == sorted(expected)


@pytest.mark.parametrize("wells,expected", (
    ([1,1,3], r'^\.*\#{1}\.+\#{1}\.+\#{3}\.*$'),
))
def test_form_a_valid_regex(wells, expected):
    assert form_a_valid_regex(wells) == expected

@pytest.mark.parametrize("line,wells,expected", (
    ('???.###', [1,1,3], ['#.#.###']),
    ('?###????????', [3,2,1], ['.###.##.#...', '.###.##..#..', '.###.##...#.', '.###.##....#', '.###..##.#..', '.###..##..#.', '.###..##...#', '.###...##.#.', '.###...##..#', '.###....##.#',]),  
))
def test_get_combinations(line, wells, expected):
    assert sorted(get_valid_combinations(line, wells)) == sorted(expected)


def test_run_part_1():
    assert run_part_1('day12/input/test_file.txt') == 21


def test_run_part_2():
    pass