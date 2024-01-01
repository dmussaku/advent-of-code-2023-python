import pytest

from .main import run_part_1, run_part_2, read_input, expand_universe, get_galaxy_pairs, Galaxy, calculate_distance


@pytest.fixture
def initial_universe():
    return [
        ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.']
    ]


@pytest.fixture
def expanded_universe():
    return [
        [char for char in "....#........"],
        [char for char in ".........#..."],
        [char for char in "#............"],
        [char for char in "............."],
        [char for char in "............."],
        [char for char in "........#...."],
        [char for char in ".#..........."],
        [char for char in "............#"],
        [char for char in "............."],
        [char for char in "............."],
        [char for char in ".........#..."],
        [char for char in "#....#......."]
    ]


def test_read_input(initial_universe):
    assert read_input("day11/input/test_file.txt") == initial_universe


def test_expand_universe(initial_universe, expanded_universe):
    expand_universe(initial_universe)
    assert initial_universe == expanded_universe


def test_get_galaxy_pairs(expanded_universe):
    galaxy_pairs = get_galaxy_pairs(expanded_universe)
    assert len(galaxy_pairs) == 36


@pytest.mark.parametrize('galaxy1, galaxy2, distance', (
    (Galaxy(row=0, column=4), Galaxy(row=10, column=9), 15),
    (Galaxy(row=2, column=0), Galaxy(row=7, column=12), 17),
    (Galaxy(row=11, column=0), Galaxy(row=11, column=5), 5),
))
def test_get_distance(galaxy1, galaxy2, distance):
    assert calculate_distance(galaxy1, galaxy2) == distance


def test_run_part_1():
    assert run_part_1("day11/input/test_file.txt") == 374


def test_run_part_2():
    pass