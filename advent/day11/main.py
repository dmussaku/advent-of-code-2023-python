from typing import List, Tuple
from itertools import combinations, count
from dataclasses import dataclass, field


@dataclass
class Galaxy:
    num: int = field(default_factory=count().__next__, init=False)
    row: int
    column: int


def read_input(file_path) -> List[List[str]]:
    matrix = []
    with open(file_path, 'r') as f:
        for line in f.read().splitlines():
            matrix.append([char for char in line])

    return matrix


def expand_universe(matrix: List[List[str]]) -> List[List[str]]:
    rows_to_add = []
    columns_to_add = []
    
    for i, row in enumerate(matrix):
        if "".join(row) == "." * len(row):
            rows_to_add.append(i)
    
    for i, column in enumerate(zip(*matrix)):
        if "".join(column) == "." * len(column):
            columns_to_add.append(i)
    i = 0
    for row in rows_to_add:
        matrix.insert(row + i, ["." for _ in range(len(matrix[0]))])
        i += 1

    i = 0
    for column in columns_to_add:
        for row in matrix:
            row.insert(column + i, ".")
        i += 1


def get_galaxy_pairs(matrix: List[List[str]]) -> List[Tuple[Galaxy, Galaxy]]:
    galaxies = []
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if matrix[i][j] == "#":
                galaxies.append(Galaxy(row=i, column=j))
    
    return list(combinations(galaxies, 2))


def calculate_distance(galaxy1: Galaxy, galaxy2: Galaxy) -> int:
    return abs(galaxy1.row - galaxy2.row) + abs(galaxy1.column - galaxy2.column)


def run_part_1(file_path):
    universe = read_input(file_path)
    expand_universe(universe)
    galaxy_pairs = get_galaxy_pairs(universe)
    return sum([calculate_distance(*galaxy_pair) for galaxy_pair in galaxy_pairs])


def run_part_2(file_path):
    pass


