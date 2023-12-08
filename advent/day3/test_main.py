import pytest

from .main import (
    Digit,
    run_part_1,
    run_part_2,
    build_matrix,
    create_digits,
)
from advent.utils import read_input_from_file


@pytest.fixture
def matrix():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


@pytest.fixture
def digit():
    return Digit("467", (0, 2), 0)


def test_build_matrix(matrix):
    input_matrix = build_matrix(read_input_from_file("day3/input/test_file.txt"))
    assert input_matrix == matrix


@pytest.mark.parametrize(
    "position,value,x,y",
    [
        (0, "467", (0, 2), 0),
        (1, "114", (5, 7), 0),
        (2, "35", (2, 3), 2),
        (3, "633", (6, 8), 2),
        (4, "617", (0, 2), 4),
        (5, "58", (7, 8), 5),
        (6, "592", (2, 4), 6),
        (7, "755", (6, 8), 7),
        (8, "664", (1, 3), 9),
        (9, "598", (5, 7), 9),
    ],
)
def test_create_digits(matrix, position, value, x, y):
    digits = create_digits(matrix)
    assert len(digits) == 10
    assert digits[position].value == value
    assert digits[position].x == x
    assert digits[position].y == y


def test_digit_positions_to_check(digit):
    assert list(digit.positions_to_check((10, 10))) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]

@pytest.mark.parametrize('digit,expected_result', [
    (Digit("467", (0, 2), 0), True),
    (Digit("114", (5, 7), 0), False),
    (Digit("35", (2, 3), 2), True),
    (Digit("633", (6, 8), 2), True),
    (Digit("617", (0, 2), 4), True),
    (Digit("58", (7, 8), 5), False),
    (Digit("592", (2, 4), 6), True),
    (Digit("755", (6, 8), 7), True),
    (Digit("664", (1, 3), 9), True),
    (Digit("598", (5, 7), 9), True),
])
def test_digit_is_adjacent_to_char(matrix, digit, expected_result):
    assert digit.is_adjacent_to_char(matrix) is expected_result


def test_run_part_1():
    assert run_part_1(read_input_from_file("day3/input/test_file.txt")) == 4361


def test_run_part_2():
    result = run_part_2(read_input_from_file("day3/input/test_file.txt"))
    assert result == 467835
