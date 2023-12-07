
def read_input_from_file(path: str):
    with open(path) as file:
        return list(file.readlines())