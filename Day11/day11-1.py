from copy import deepcopy

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def convert_input_to_matrix(input):
    matrix = []
    for line in input:
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)
    return matrix

def is_within_bounds(matrix, row, col, i, j):
    num_rows = len(matrix)
    num_cols = len(matrix[row])
    are_not_both_zero = i != 0 or j != 0
    row_within_bounds = 0 <= row + i < num_rows
    col_within_bounds = 0 <= col + j < num_cols
    return are_not_both_zero and row_within_bounds and col_within_bounds

def count_occupied_adjacent(matrix, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_within_bounds(matrix, row, col, i, j):
                if matrix[row+i][col+j] == "#":
                    count += 1
    return count
                

def run_simulation(matrix):
    changes_occured = False
    new_matrix = deepcopy(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            num_occupied_adjacent = count_occupied_adjacent(matrix, row, col)
            if matrix[row][col] == "L" and num_occupied_adjacent == 0:
                changes_occured = True
                new_matrix[row][col] = "#"
            elif matrix[row][col] == "#" and num_occupied_adjacent >= 4:
                changes_occured = True
                new_matrix[row][col] = "L"
    return changes_occured, new_matrix

def count_occupied_seats(matrix):
    count = 0
    for row in range(len(matrix)):
        count += sum([1 for col in range(len(matrix[row])) if matrix[row][col] == "#"])
    return count

def main():
    input = fetch_input()
    matrix = convert_input_to_matrix(input)
    repeat = True
    while(repeat):
        repeat, matrix = run_simulation(matrix)
    occupied_seats = count_occupied_seats(matrix)
    print(occupied_seats)
    

main()
