from day2.main import run_part_1 as day2_part1, run_part_2 as day2_part2
from day3.main import run_part_1 as day3_part1, run_part_2 as day3_part2
from day4.main import run_part_1 as day4_part1, run_part_2 as day4_part2
from utils import read_input_from_file


def main():
    print("Day 2 part 1: ", day2_part1(read_input_from_file("day2/input/file.txt")))
    print("Day 2 part 2: ", day2_part2(read_input_from_file("day2/input/file.txt")))
    print("Day 3 part 1: ", day3_part1(read_input_from_file("day3/input/file.txt")))
    print("Day 3 part 2: ", day3_part2(read_input_from_file("day3/input/file.txt")))
    print("Day 4 part 1: ", day4_part1(read_input_from_file("day4/input/file.txt")))
    print("Day 4 part 2: ", day4_part2(read_input_from_file("day4/input/file.txt")))

if __name__ == "__main__":
    main()
