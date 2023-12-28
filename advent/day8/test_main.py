from .main import run_part_1, run_part_2, parse_input


def test_parse_input():
    assert parse_input("day8/input/test_file.txt") == (
        "LLR",
        {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        },
    )


def test_run_part_1():
    assert run_part_1("day8/input/test_file.txt") == 6


def test_run_part_2():
    pass