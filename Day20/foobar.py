import re
import sys
sys.path.append("..")
from input_reader import InputReader
from matrix_utils import MatrixUtils
import math

class Neighbor:
    def __init__(self, tile_name, direction):
        self.tile_name = tile_name
        self.direction = direction

    def __eq__(self, other):
        return self.tile_name == other.tile_name and self.direction == other.direction

    def __str__(self):
        return self.tile_name + " " + self.direction

    def __hash__(self):
        return int(self.tile_name.split(" ")[1][:-1])

    def rotate_clockwise(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

    def flip_y(self):
        if self.direction == "N":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "N"

    def flip_x(self):
        if self.direction == "E":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "E"

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
    return matches == len(arr1)

def index_to_direction(index):
    if index == 0:
        return "N"
    elif index == 1:
        return "S"
    elif index == 2:
        return "W"
    else:
        return "E"

def are_neighbors(tile_name1, tile_name2, tiles):
    tile1 = tiles[tile_name1]
    tile2 = tiles[tile_name2]
    tile_1_rows_and_columns = [tile1[0], tile1[len(tile1) - 1], MatrixUtils.get_column(tile1, 0), MatrixUtils.get_column(tile1, len(tile1) - 1)]
    tile_2_rows_and_columns = [tile2[0], tile2[len(tile2) - 1], MatrixUtils.get_column(tile2, 0), MatrixUtils.get_column(tile2, len(tile2) - 1)]
    for index1, row_col1 in enumerate(tile_1_rows_and_columns):
        for index2, row_col2 in enumerate(tile_2_rows_and_columns):
            if arrays_match(row_col1, row_col2) or arrays_match(row_col1, reversed(row_col2)):
                return Neighbor(tile_name1, index_to_direction(index2)), Neighbor(tile_name2, index_to_direction(index1))
    return None, None

def find_neighbors(tiles):
    tile_to_neighbor = {}
    for tile_name in tiles:
        tile_to_neighbor[tile_name] = set()
    for tile_name1 in tiles:
        for tile_name2 in tiles:
            if tile_name1 != tile_name2:
                neighbor1, neighbor2 = are_neighbors(tile_name1, tile_name2, tiles)
                if neighbor2 != None:
                    tile_to_neighbor[tile_name1].add(neighbor2)
                if neighbor1 != None:
                    tile_to_neighbor[tile_name2].add(neighbor1)
    return tile_to_neighbor

def find_corner(neighbors):
    for tile_name in neighbors:
        if len(neighbors[tile_name]) == 2:
            return tile_name

def are_south_east(neighbors):
    curr_string = ""
    for neighbor in neighbors:
        curr_string += neighbor.direction
    return "SE" in curr_string or "ES" in curr_string

def rotate_neighbors(neighbors):
    for neighbor in neighbors:
        neighbor.rotate_clockwise()

def flip_y_neighbors(neighbors):
    for neighbor in neighbors:
        neighbor.flip_y()
    
def flip_x_neighbors(neighbors):
    for neighbor in neighbors:
        neighbor.flip_x()

def previous_is_west(curr_tile_name, previous_tile_name, neighbors):
    for neighbor in neighbors[curr_tile_name]:
        if neighbor.tile_name == previous_tile_name:
            return neighbor.direction == "W"
    print("THIS SHOULD NEVER EXECUTE")
    return False

def first_corner(tiles, neighbors, curr_tile_name):
    while not are_south_east(neighbors[curr_tile_name]):
        rotate_neighbors(neighbors[curr_tile_name])
        tiles[curr_tile_name] = MatrixUtils.rotate_clockwise(tiles[curr_tile_name])

def match_previous_neighbor(tiles, neighbors, curr_tile_name, previous_tile_name):
    while not previous_is_west(curr_tile_name, previous_tile_name, neighbors):
        rotate_neighbors(neighbors[curr_tile_name])
        tiles[curr_tile_name] = MatrixUtils.rotate_clockwise(tiles[curr_tile_name])
    curr_tile_west_col = MatrixUtils.get_column(tiles[curr_tile_name], 0)
    prev_tile_east_col = MatrixUtils.get_column(tiles[previous_tile_name], len(tiles[previous_tile_name]) - 1)
    if not arrays_match(curr_tile_west_col, prev_tile_east_col):
        tiles[curr_tile_name] = MatrixUtils.invert_y(tiles[curr_tile_name])
        flip_y_neighbors(neighbors[curr_tile_name])

def flip_north_neighbor(neighbors, tiles, curr_tile_name):
    for neighbor in neighbors:
        if neighbor.direction == "N":
            neighbor.flip_y()
            tiles[curr_tile_name] = MatrixUtils.invert_y(tiles[curr_tile_name])
            flip_y_neighbors(neighbors)

def find_directional_neighbor(neighbors, direction):
    for neighbor in neighbors:
        if neighbor.direction == direction:
            return neighbor.tile_name
    return None

def find_east_neighbor(neighbors):
    return find_directional_neighbor(neighbors, "E")

def find_south_neighbor(neighbors):
    return find_directional_neighbor(neighbors, "S")

def find_north_neighbor(neighbors):
    return find_directional_neighbor(neighbors, "N")

def flatten_picture(order, tiles):
    number_tiles = int(math.sqrt(len(tiles)))
    chars_per_row = len(tiles[order[0][0]])
    width_length = number_tiles * chars_per_row
    result = [["~" for _ in range(width_length)] for _ in range(width_length)]
    for row_index, row in enumerate(order):
        for column_index, tile_name in enumerate(row):
            tile = tiles[tile_name]
            for tile_row_index, tile_row in enumerate(tile):
                for tile_col_index, char in enumerate(tile_row):
                    result[tile_row_index + (chars_per_row * row_index)][tile_col_index + (chars_per_row * column_index)] = char
    return result

def match_above_tile(tiles, neighbors, curr_tile_name, above_tile_name):
    while find_north_neighbor(neighbors[curr_tile_name]) != above_tile_name:
        rotate_neighbors(neighbors[curr_tile_name])
        tiles[curr_tile_name] = MatrixUtils.rotate_clockwise(tiles[curr_tile_name])
    curr_tile_north_row = tiles[curr_tile_name][0]
    above_tile_south_row = tiles[above_tile_name][len(tiles[above_tile_name]) - 1]
    if not arrays_match(curr_tile_north_row, above_tile_south_row):
        tiles[curr_tile_name] = MatrixUtils.invert_x(tiles[curr_tile_name])
        flip_x_neighbors(neighbors[curr_tile_name])

def strip_edges(tiles):
    new_tiles = {}
    for tile_name in tiles:
        new_tile = []
        tile = tiles[tile_name]
        for row in tile[1: len(tile) - 1]:
            new_row = []
            for value in row[1:len(row) - 1]:
                new_row.append(value)
            new_tile.append(new_row)
        new_tiles[tile_name] = new_tile
    return new_tiles
        
def build_picture(neighbors, tiles):
    curr_tile_name = find_corner(neighbors)
    order = []
    running_row = []
    counter = 0
    previous_tile_name = None
    # handle first row
    while(counter < math.sqrt(len(tiles))):
        if previous_tile_name is None:
            first_corner(tiles, neighbors, curr_tile_name)
        else:
            match_previous_neighbor(tiles, neighbors, curr_tile_name, previous_tile_name)
            flip_north_neighbor(neighbors[curr_tile_name], tiles, curr_tile_name)
        running_row.append(curr_tile_name)
        previous_tile_name = curr_tile_name
        curr_tile_name = find_east_neighbor(neighbors[curr_tile_name])
        counter += 1
    order.append(running_row)
    counter = 0
    above_tile_name = running_row[0]
    curr_tile_name = find_south_neighbor(neighbors[above_tile_name])
    running_row = []
    print(order)
    while curr_tile_name is not None:
        match_above_tile(tiles, neighbors, curr_tile_name, above_tile_name)
        running_row.append(curr_tile_name)
        counter += 1
        curr_tile_name = find_east_neighbor(neighbors[curr_tile_name])
        above_tile_name = find_east_neighbor(neighbors[above_tile_name])
        if counter >= math.sqrt(len(tiles)):
            order.append(running_row)
            counter = 0
            above_tile_name = running_row[0]
            curr_tile_name = find_south_neighbor(neighbors[above_tile_name])
            running_row = []
    order.append(running_row)
    tiles = strip_edges(tiles)
    picture = flatten_picture(order, tiles)
    MatrixUtils.print_matrix(MatrixUtils.invert_x(MatrixUtils.rotate_clockwise(MatrixUtils.invert_y(picture))))
    return picture

def is_monster(picture, monster_coords, x, y):
    for (y_offset, x_offset) in monster_coords:
        curr_x = x + x_offset
        curr_y = y + y_offset
        if curr_x < 0 or curr_x >= len(picture) or curr_y < 0 or curr_y >= len(picture) or picture[curr_x][curr_y] != "#":
            return False
    return True

def fill_monster(picture, monster_coords, x, y):
    for (y_offset, x_offset) in monster_coords:
        curr_x = x + x_offset
        curr_y = y + y_offset
        picture[curr_x][curr_y] = "0"

def determine_roughness(picture):
                      # 
    #    ##    ##    ###
     #  #  #  #  #  #  
    monster_coords = [
        (-18, 1),
        (-13, 1),
        (-12, 1),
        (-7, 1),
        (-6, 1),
        (-1, 1),
        (0, 1),
        (1, 1),
        (-17, 2),
        (-14, 2),
        (-11, 2),
        (-8, 2),
        (-5, 2),
        (-2, 2)
    ]
    monster_count = 0
    water_roughness = 0
    for row_index, row in enumerate(picture):
        for col_index, value in enumerate(row):
            if value == "#":
                if is_monster(picture, monster_coords, row_index, col_index):
                    fill_monster(picture, monster_coords, row_index, col_index)
                    monster_count += 1
                else:
                    water_roughness += 1
    return monster_count, water_roughness

def calculate(picture):
    num_monsters = 0
    water_roughness = 0
    counter = 0
    while num_monsters == 0:
        num_monsters, water_roughness = determine_roughness(picture)
        if num_monsters == 0:
            picture = MatrixUtils.rotate_clockwise(picture)
        counter += 1
        if counter % 16 == 0:
            picture = MatrixUtils.invert_y(picture)
        if counter % 4 == 0:
            picture = MatrixUtils.invert_x(picture)
    print(water_roughness)

def main():
    line_sets = InputReader.fetch_input_seperated_by_empty_lines()
    tiles = lines_to_tiles(line_sets)
    neighbors = find_neighbors(tiles)
    picture = build_picture(neighbors,tiles)
    calculate(picture)

main()
