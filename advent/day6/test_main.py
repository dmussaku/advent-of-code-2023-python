import pytest

from .main import run_part_1, run_part_2, parse_times_and_distances, distance_traveled, winning_possibilities

@pytest.mark.parametrize('button_held_time,max_time,expected', (
    (0, 7, 0),
    (1, 7, 6),
    (2, 7, 10),
    (3, 7, 12),
    (4, 7, 12),
    (5, 7, 10),
    (6, 7, 6),
    (7, 7, 0),
))
def test_distance_traveled(button_held_time, max_time, expected):
    assert distance_traveled(button_held_time, max_time) == expected


def test_parse_times_and_distances():
    result = parse_times_and_distances('day6/input/test_file.txt')
    assert result == [(7, 9), (15,40), (30, 200)]

@pytest.mark.parametrize('max_time,win_distance,expected', (
    (7, 9, 4),
    (15, 40, 8),
    (30, 200, 9),
  
))
def test_winning_possibilities(max_time, win_distance, expected):
    result = winning_possibilities(7, 9)
    assert len(result) == 4

def test_run_part_1():
    assert run_part_1('day6/input/test_file.txt') == 288


def test_run_part_2():
    pass