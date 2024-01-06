from day2.main import run_part_1 as day2_part1, run_part_2 as day2_part2
from day3.main import run_part_1 as day3_part1, run_part_2 as day3_part2
from day4.main import run_part_1 as day4_part1, run_part_2 as day4_part2
from day5.main import run_part_1 as day5_part1, run_part_2 as day5_part2
from day6.main import run_part_1 as day6_part1, run_part_2 as day6_part2
from day7.main import run_part_1 as day7_part1, run_part_2 as day7_part2
from day8.main import run_part_1 as day8_part1, run_part_2 as day8_part2
from day9.main import run_part_1 as day9_part1, run_part_2 as day9_part2
from day11.main import run_part_1 as day11_part1, run_part_2 as day11_part2
from utils import read_input_from_file


def main():
    print("Day 2 part 1: ", day2_part1(read_input_from_file("day2/input/file.txt")))
    print("Day 2 part 2: ", day2_part2(read_input_from_file("day2/input/file.txt")))
    print("Day 3 part 1: ", day3_part1(read_input_from_file("day3/input/file.txt")))
    print("Day 3 part 2: ", day3_part2(read_input_from_file("day3/input/file.txt")))
    print("Day 4 part 1: ", day4_part1(read_input_from_file("day4/input/file.txt")))
    print("Day 4 part 2: ", day4_part2(read_input_from_file("day4/input/file.txt")))
    print("Day 5 part 1: ", day5_part1("day5/input/file.txt"))
    # print("Day 5 part 2: ", day5_part2("day5/input/file.txt"))
    print("Day 6 part 1: ", day6_part1("day6/input/file.txt"))
    # print("Day 6 part 2: ", day6_part2("day6/input/file.txt")) # slow af
    print("Day 7 part 1: ", day7_part1("day7/input/file.txt"))
    # print("Day 7 part 2: ", day7_part2("day7/input/file.txt"))
    print("Day 8 part 1: ", day8_part1("day8/input/file.txt"))
    print("Day 9 part 1: ", day9_part1("day9/input/file.txt"))
    print("Day 9 part 2: ", day9_part2("day9/input/file.txt"))
    print("Day 11 part 1: ", day11_part1("day11/input/file.txt"))


if __name__ == "__main__":
    main()
