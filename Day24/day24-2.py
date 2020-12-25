import re
import sys
sys.path.append("..")
from input_reader import InputReader

import pprint

printer = pprint.PrettyPrinter()

def get_directions(tile):
    directions = []
    index = 0
    while index < len(tile):
        if tile[index] == "e" or tile[index] == "w":
            directions.append(tile[index])
        else:
            curr_dir = tile[index]
            if index + 1 < len(tile) and (tile[index + 1] == "e" or tile[index + 1] == "w"):
                index += 1
                curr_dir += tile[index]
            directions.append(curr_dir)
        index += 1
    return directions

def get_coords(tile):
    directions = get_directions(tile)
    x = 0
    y = 0
    for direction in directions:
        if direction == "ne":
            y += 2
        elif direction == "e":
            y += 1
            x += 1
        elif direction == "se":
            y -= 1
            x += 1
        elif direction == "sw":
            y -= 2
        elif direction == "w":
            y -= 1
            x -= 1
        else:
            y += 1
            x -= 1
    return x, y

def coords_to_key(x, y):
    return str(x) + "," + str(y)

def key_to_coords(key):
    coords = key.split(",")
    return int(coords[0]), int(coords[1])

def find_black_tiles(tiles):
    black_tiles = set()
    for tile in tiles:
        x, y = get_coords(tile)
        key = coords_to_key(x, y)
        if key in black_tiles:
            black_tiles.remove(key)
        else:
            black_tiles.add(key)
    return black_tiles

def initalize_grid(rounds):
    return [[False for i in range(8*rounds)] for j in range(4*rounds)]

def set_black_tiles(rounds):
    tiles = InputReader.fetch_input_lines()
    black_tiles = find_black_tiles(tiles)
    grid = initalize_grid(rounds)
    for black_tile in black_tiles:
        x_offset, y_offset = key_to_coords(black_tile)
        x = (2 * rounds) + x_offset
        y = (2 * rounds) + y_offset
        grid[x][y] = True
    return grid

def is_active(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == True

def count_active_neighbors(x, y, grid):
    directions = ["e", "w", "ne", "nw", "se", "sw"]
    active_neighbors = 0
    for direction in directions:
        x_offset, y_offset = get_coords(direction)
        if is_active(x + x_offset, y + y_offset, grid):
            active_neighbors += 1
    return active_neighbors

def simulate(rounds, grid):
    for round in range(rounds):
        new_grid = initalize_grid(rounds)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                num_neighbors = count_active_neighbors(x, y, grid)
                if grid[x][y] == True and (num_neighbors == 0 or num_neighbors > 2):
                    new_grid[x][y] = False
                elif grid[x][y] == False and num_neighbors == 2:
                    new_grid[x][y] = True
                else:
                    new_grid[x][y] = grid[x][y]
        grid = new_grid
        # print(round + 1)
        # print(count_black_tiles(grid))
        # print("")
    return grid

def count_black_tiles(grid):
    black_tiles = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                black_tiles += 1
    return black_tiles

def main():
    rounds = 100
    grid = set_black_tiles(rounds)
    grid = simulate(rounds, grid)
    print(count_black_tiles(grid))

main()
