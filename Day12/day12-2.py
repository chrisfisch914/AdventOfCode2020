def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def rotate_ninety(waypoint_north, waypoint_east):
    return -waypoint_east, waypoint_north

def rotate(waypoint_north, waypoint_east, degree):
    num_rotates = degree / 90
    for i in range(num_rotates):
        waypoint_north, waypoint_east = rotate_ninety(waypoint_north, waypoint_east)
    return waypoint_north, waypoint_east

def cal_man_dist(north, east):
    return abs(north) + abs(east)

def compute_north_east(input):
    ship_north = 0
    ship_east = 0
    waypoint_north = 1
    waypoint_east = 10
    for line in input:
        heading = line[0]
        dist = int(line[1:])
        if heading == "F":
            ship_north += (waypoint_north * dist)
            ship_east += (waypoint_east * dist)
        elif heading == "N":
            waypoint_north += dist
        elif heading == "S":
            waypoint_north -= dist
        elif heading == "E":
            waypoint_east += dist
        elif heading == "W":
            waypoint_east -= dist
        elif heading == "R":
            waypoint_north, waypoint_east = rotate(waypoint_north, waypoint_east, dist)
        elif heading == "L":
            waypoint_north, waypoint_east = rotate(waypoint_north, waypoint_east, 360 - dist)
    return ship_north, ship_east
 
def main():
    input = fetch_input()
    north, east = compute_north_east(input)
    print(cal_man_dist(north, east))
main()
