def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def rotate_ninety(curr_dir):
    if curr_dir == "E":
        return "S"
    if curr_dir == "S":
        return "W"
    if curr_dir == "W":
        return "N"
    if curr_dir == "N":
        return "E"

def rotate(curr_dir, degree):
    num_rotates = degree / 90
    for i in range(num_rotates):
        curr_dir = rotate_ninety(curr_dir)
    return curr_dir

def cal_man_dist(north, east):
    return abs(north) + abs(east)

def compute_north_east(input):
    north = 0
    east = 0
    direction = "E"
    for line in input:
        heading = line[0]
        dist = int(line[1:])
        if heading == "F":
            heading = direction
        if heading == "N":
            north += dist
        elif heading == "S":
            north -= dist
        elif heading == "E":
            east += dist
        elif heading == "W":
            east -= dist
        elif heading == "R":
            direction = rotate(direction, dist)
        elif heading == "L":
            direction = rotate(direction, 360 - dist)
    return north, east
 
def main():
    input = fetch_input()
    north, east = compute_north_east(input)
    print(cal_man_dist(north, east))


main()
