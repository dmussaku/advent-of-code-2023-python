from typing import List

def print_matrix(matrix: List[List[int]]):
    largest_len = len(" ".join([str(fig) for fig in matrix[0]]))
    for array in matrix:
        print(" ".join([str(fig) for fig in array]).center(largest_len))
    print()


def parse_input(file_path: str) -> List[List[int]]:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    return [[int(fig) for fig in line.split(" ")] for line in lines]


def create_prediction_matrix(input_list: List[int]) -> List[List[int]]:
    matrix = [input_list]
    
    while not all(v==0 for v in matrix[-1]):
        next_line = []
        for i in range(len(matrix[-1]) - 1):
            next_line.append(matrix[-1][i+1] - matrix[-1][i])
        matrix.append(next_line)
    
    return matrix
    


def run_part_1(file_path):
    input_arrays = parse_input(file_path)
    result = 0
    
    for i, input_array in enumerate(input_arrays):
        matrix = create_prediction_matrix(input_array)
        # print_matrix(matrix)
        interim_result = sum([array[-1] for array in matrix])
        # print(interim_result)
        # print('-' * 60)
        result += interim_result
    
    print()
    return result


def run_part_2(file_path):
    pass


