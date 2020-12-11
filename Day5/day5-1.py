import math

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def get_row(row_info):
    lo = 0
    hi = 127
    for index in range(len(row_info)):
        dist = (hi - lo + 1) / 2
        if row_info[index] == "F":
            hi -= dist
        else:
            lo += dist
    return lo

def get_col(col_info):
    lo = 0
    hi = 7
    for index in range(len(col_info)):
        dist = (hi - lo + 1) / 2
        if col_info[index] == "L":
            hi -= dist
        else:
            lo += dist
    return lo

def main():
    input = fetch_input()
    result = 0
    for line in input:
        row = get_row(line[0: 7])
        col = get_col(line[7:])
        seat_id = row * 8 + col
        result = max(result, seat_id)
    print(result)

main()
