from typing import Tuple, Dict


def parse_input(file_path) -> Tuple[str, Dict]:
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    instructions = lines[0]
    
    node_map = {}
    for line in lines[2:]:
        parent = line.split("=")[0].strip()
        left_child, right_child = line.split("=")[1].strip().strip('(').strip(')').split(", ")
        node_map[parent] = (left_child, right_child)
    
    return instructions, node_map


def run_part_1(file_path):
    instructions, node_map = parse_input(file_path)
    
    is_zzz_found = False
    current_node = 'AAA'
    num_steps = i = 0
    
    while is_zzz_found == False:
        try:
            next_position = 0 if instructions[i] == 'L' else 1
        except IndexError:
            i = 0
            continue
        
        current_node = node_map[current_node][next_position]
        num_steps += 1
        i += 1
        
        if current_node == 'ZZZ':
            is_zzz_found = True

    return num_steps

def run_part_2(input):
    pass


