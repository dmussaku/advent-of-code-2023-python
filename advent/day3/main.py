from dataclasses import dataclass
from typing import Optional


@dataclass
class Digit:
    value: str
    x: tuple[int, int]
    y: int
    gear_position: Optional[tuple[int, int]] = None

    def __repr__(self):
        return f"Digit({self.value}, {self.x}, {self.y}, {self.gear_position})"

    def __str__(self):
        return f"{self.value}"

    def positions_to_check(self, max_matrix_dimensions: tuple[int, int]):
        max_x, max_y = max_matrix_dimensions
        for x in range(max(0, self.x[0] - 1), min(max_x, self.x[1] + 2)):
            for y in range(max(0, self.y - 1), min(max_y, self.y + 2)):
                yield (x, y)

    def is_adjacent_to_char(self, matrix: list[list[str]]):
        # any character that is not digit or .
        for x, y in self.positions_to_check((len(matrix[0]), len(matrix))):
            if matrix[y][x].isdigit() or matrix[y][x] == ".":
                continue
            else:
                return True
        return False

    def find_gear_position(self, matrix: list[list[str]]):
        for x, y in self.positions_to_check((len(matrix[0]), len(matrix))):
            if matrix[y][x] == "*":
                self.gear_position = (x, y)
                return


def build_matrix(input_lines):
    matrix = []
    for line in input_lines:
        matrix.append(line)
    return matrix


def create_digits(matrix):
    digits = []
    current_digit = None
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char.isdigit():
                if current_digit is None:
                    current_digit = Digit(char, (x, x), y)
                else:
                    current_digit.value += char
                    current_digit.x = (current_digit.x[0], x)
                    current_digit.y = y
            else:
                if current_digit is not None:
                    digits.append(current_digit)
                    current_digit = None
    return digits


def run_part_1(input_lines):
    input_matrix = build_matrix(input_lines)
    digits = create_digits(input_matrix)
    return sum(
        int(digit.value)
        for digit in filter(lambda x: x.is_adjacent_to_char(input_matrix), digits)
    )


def run_part_2(input_lines):
    input_matrix = build_matrix(input_lines)
    digits = create_digits(input_matrix)
    for digit in digits:
        digit.find_gear_position(input_matrix)

    digits_adjacent_to_gear = list(
        filter(lambda x: x.gear_position is not None, digits)
    )

    digit_pairs = []
    for i, digit in enumerate(digits_adjacent_to_gear):
        for j in range(i + 1, len(digits_adjacent_to_gear)):
            other_digit = digits_adjacent_to_gear[j]
            if digit.gear_position == other_digit.gear_position:
                digit_pairs.append((digit, other_digit))
    return sum(
        int(digit.value) * int(other_digit.value) for digit, other_digit in digit_pairs
    )
