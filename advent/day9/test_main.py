from .main import run_part_1, run_part_2, parse_input, create_prediction_matrix
from advent.utils import read_input_from_file


def test_parse_input():
    assert parse_input("day9/input/test_file.txt") == [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]

def test_create_prediction_matrix():
    assert create_prediction_matrix([0, 3, 6, 9, 12, 15]) == [
        [0, 3, 6, 9, 12, 15],
        [3, 3, 3, 3, 3],
        [0, 0, 0, 0],
    ]


def test_run_part_1():
    assert run_part_1("day9/input/test_file.txt") == 114


def test_run_part_2():
    assert run_part_2("day9/input/test_file.txt") == 2