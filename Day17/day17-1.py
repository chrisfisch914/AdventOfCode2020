import re

ROUNDS = 6

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def parse_input(input):
    lookup = {}
    for x in range(len(input)):
        for y in range(len(input[x])):
            key = coords_to_key(x, y, 0)
            lookup[key] = input[x][y] == "#"
    return lookup

def coords_to_key(x, y, z):
    return str(x) + ", " + str(y) + ", " + str(z)

def count_active_neighbors(lookup, x, y, z):
    count = 0
    for x_inc in range(-1, 2):
        for y_inc in range(-1, 2):
            for z_inc in range(-1, 2):
                if x_inc != 0 or y_inc != 0 or z_inc != 0:
                    key = coords_to_key(x + x_inc, y + y_inc, z + z_inc)
                    if key in lookup and lookup[key] == True:
                        count += 1
    return count

def run_round(lookup, curr_round, x_y_dist):
    new_lookup = {}
    for x in range(-x_y_dist, x_y_dist + 1):
        for y in range(-x_y_dist, x_y_dist + 1):
            for z in range(-curr_round, curr_round + 1):
                active_neighbors = count_active_neighbors(lookup, x, y, z)
                key = coords_to_key(x, y, z)
                if key not in lookup:
                    lookup[key] = False
                is_active = lookup[key]
                if is_active:
                    new_lookup[key] = 2 <= active_neighbors <= 3
                else:
                    new_lookup[key] = active_neighbors == 3
    return new_lookup

def count_active_cubes(lookup):
    return sum([1 for value in lookup.values() if value])

def main():
    input = fetch_input()
    length_and_width = len(input)
    lookup = parse_input(input)
    for i in range(1, ROUNDS + 1):
        lookup = run_round(lookup, i, length_and_width + i)
    print(count_active_cubes(lookup))

main()
