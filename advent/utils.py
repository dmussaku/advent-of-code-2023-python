def read_input_from_file(path: str):
    with open(path) as file:
        return [line.strip("\n") for line in file.readlines()]
