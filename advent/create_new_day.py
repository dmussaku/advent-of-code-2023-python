import os

# create a terminal command that creates a new day which is a directory that will be named dayX where X is a day number and will contain an input directory with 2 files (file.txt and test_file.txt) and a main.py and test_main.py files
# the main.py file will contain a run_part_1 and run_part_2 functions that will be imported in the main.py file in the advent directory
# the test_main.py file will contain a test_run_part_1 and test_run_part_2 functions that will be imported in the test_main.py file in the advent directory
# the input/file.txt will contain the input for the day
# the input/test_file.txt will contain the test input for the day


def create_new_day(day_number):
    # create the day directory
    os.mkdir(f"day{day_number}")
    # create the input directory
    os.mkdir(f"day{day_number}/input")
    # create the main.py file
    with open(f"day{day_number}/main.py", "w") as f:
        f.write(
            f"from utils import read_input_from_file\n\n\ndef run_part_1(input):\n    pass\n\n\ndef run_part_2(input):\n    pass\n\n\n"
        )
    # create the test_main.py file
    with open(f"day{day_number}/test_main.py", "w") as f:
        f.write(
            f"from day{day_number}.main import run_part_1, run_part_2\nfrom utils import read_input_from_file\n\n\ndef test_run_part_1():\n    pass\n\n\ndef test_run_part_2():\n    pass"
        )
    # create the input/file.txt file
    with open(f"day{day_number}/input/file.txt", "w") as f:
        f.write("")
    # create the input/test_file.txt file
    with open(f"day{day_number}/input/test_file.txt", "w") as f:
        f.write("")

    print(f"Day{day_number} directory created successfully!")


if __name__ == "__main__":
    day_number = int(input("Enter day number: "))
    create_new_day(day_number)
