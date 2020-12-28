import re
import sys
sys.path.append("..")
from input_reader import InputReader
import pprint

printer = pprint.PrettyPrinter()

def lines_to_tiles(line_sets):
    tiles = {}
    for lines in line_sets:
        lines = lines.split("\n")
        tile = []
        tile_name = lines[0]
        lines = lines[1:]
        for line in lines:
            row = []
            for char in line:
                    row.append(char)
            tile.append(row)
        tiles[tile_name] = (tile)
    return tiles

def arrays_match(arr1, arr2):
    matches = sum([1 for (a,b) in zip(arr1, arr2) if a == b])
    reverse_matches = sum([1 for (a,b) in zip(arr1, reversed(arr2)) if a == b])
    return matches == len(arr1) or reverse_matches == len(arr2)

def get_column(tile, col):
    return [tile[row][col] for row in range(len(tile))]

def are_neighbors(tile1, tile2):
    tile_1_rows_and_columns = [tile1[0], tile1[len(tile1) - 1], get_column(tile1, 0), get_column(tile1, len(tile1) - 1)]
    tile_2_rows_and_columns = [tile2[0], tile2[len(tile2) - 1], get_column(tile2, 0), get_column(tile2, len(tile2) - 1)]
    for row_col1 in tile_1_rows_and_columns:
        for row_col2 in tile_2_rows_and_columns:
            if arrays_match(row_col1, row_col2):
                return True

def find_neighbors(tiles):
    tile_to_neighbor = {}
    for tile_name in tiles:
        tile_to_neighbor[tile_name] = set()
    for tile_name1 in tiles:
        for tile_name2 in tiles:
            if tile_name1 != tile_name2 and are_neighbors(tiles[tile_name1], tiles[tile_name2]):
                tile_to_neighbor[tile_name1].add(tile_name2)
                tile_to_neighbor[tile_name2].add(tile_name1)
    return tile_to_neighbor

def multiply_corners(neighbors):
    result = 1
    for tile_name in neighbors:
        if len(neighbors[tile_name]) == 2:
            tile_num = int(tile_name.split(" ")[1][0: -1])
            result *= tile_num
    return result

def main():
    line_sets = InputReader.fetch_input_seperated_by_empty_lines()
    tiles = lines_to_tiles(line_sets)
    neighbors = find_neighbors(tiles)
    # printer.pprint(find_neighbors(tiles))
    print(multiply_corners(neighbors))

main()
