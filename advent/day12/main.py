import re
from itertools import product

from typing import List, Tuple


def parse_input(file_path: str) -> List[Tuple[str, List[int]]]:
    with open(file_path, 'r') as f:
        return [
            (line.split(' ')[0],
             list(map(int, line.split(' ')[1].strip('\n').split(',')))
            ) for line in f.readlines()
        ]

def get_all_combinations(line: str):
    """Get all possible combinations of wells in line
    switches ? with either . or #

    Args:
        line (str): line of characters with ? indicating unknown positions, 
                    example: "???.###"

    Returns:
         product[str]: List of all possible combinations of wells in line, 
                    example: ["###.###", "##..###", ...]
    """
    chars_to_combine = []
    for char in line:
        if char == '?':
            chars_to_combine.append('.#')
        else:
            chars_to_combine.append(char)

    for combo in product(*chars_to_combine):
        yield ''.join(combo)


def form_a_valid_regex(wells: List[int]):
    """
    """
    return r"^\.*" + r"\.+".join(rf"\#{{{well}}}" for well in wells) + r"\.*$"


def get_valid_combinations(line: str, wells: List[int]) -> List[str]:
    valid_combinations = []
    regex_pattern = form_a_valid_regex(wells)
    # print(regex_pattern)
    for combo in get_all_combinations(line):
        if re.match(regex_pattern, combo):
            valid_combinations.append(combo)
    # print(valid_combinations)
    return valid_combinations


def run_part_1(file_path):
    lines = parse_input(file_path)
    result = 0
    for line, wells in lines:
        result += len(get_valid_combinations(line, wells))
    
    return result


def run_part_2(file_path):
    pass


