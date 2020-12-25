import re
import sys
sys.path.append("..")
from input_reader import InputReader

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

def count_black_tiles(tiles):
    black_tiles = set()
    for tile in tiles:
        x, y = get_coords(tile)
        key = coords_to_key(x, y)
        if key in black_tiles:
            black_tiles.remove(key)
        else:
            black_tiles.add(key)
    return black_tiles

def main():
    tiles = InputReader.fetch_input_lines()
    black_tiles = count_black_tiles(tiles)
    print(len(black_tiles))

main()
