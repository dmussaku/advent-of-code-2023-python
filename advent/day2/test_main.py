import pytest

from advent.utils import read_input_from_file
from .main import Game, run_part_1, run_part_2


@pytest.mark.parametrize(
    "input_str,game_id,red,green,blue",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1, 4, 2, 6),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            2,
            1,
            3,
            4,
        ),
    ],
)
def test_game_new(input_str, game_id, red, green, blue):
    game = Game.new(input_str)

    assert game.game_id == game_id
    assert game.red == red
    assert game.green == green
    assert game.blue == blue


def test_run_part_1():
    input_lines = read_input_from_file("day2/input/test_file.txt")
    assert run_part_1(input_lines) == 8


def test_run_part_2():
    input_lines = read_input_from_file("day2/input/test_file.txt")
    assert run_part_2(input_lines) == 2286
