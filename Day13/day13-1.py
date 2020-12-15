def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def find_min_intersection(depart_time, curr_id):
    runner = curr_id
    while(runner < depart_time):
        runner += curr_id
    return runner

def find_bus_id(depart_time, bus_ids):
    new_depart_time = float('inf')
    min_bus_id = bus_ids[0]
    for curr_id in bus_ids:
        if curr_id == "x":
            continue
        curr_id = int(curr_id)
        curr_min = find_min_intersection(depart_time, curr_id)
        if curr_min < new_depart_time:
            new_depart_time = curr_min
            min_bus_id = curr_id
    return min_bus_id, new_depart_time

def main():
    input = fetch_input()
    depart_time = int(input[0])
    bus_ids = input[1].split(",")
    min_bus_id, new_depart_time = find_bus_id(depart_time, bus_ids)
    print(min_bus_id * (new_depart_time - depart_time))

main()
