def create_mapping(order):
    new_order = {}
    for i in range(len(order)):
        new_order[order[i]] = order[(i + 1) % len(order)]
    new_order[order[-1]] = "10"
    for i in range(10, 1000000):
        new_order[str(i)] = str(i + 1)
    new_order["1000000"] = order[0]
    return new_order

def remove_elements(order, start_value):
    removed = []
    curr_value = order[start_value]
    for i in range(3):
        removed.append(curr_value)
        curr_value = order[curr_value]
    order[start_value] = curr_value
    return removed

def determine_destination_cup(curr_num, removed):
    removed_set = set(removed)
    curr_num = int(curr_num) - 1
    while(True):
        if int(curr_num) == 0:
            curr_num = "1000000"
        if str(curr_num) not in removed_set:
            return str(curr_num)
        curr_num -= 1

def add_removed_at_destination(destination_cup, removed, order):
    order[removed[2]] = order[destination_cup]
    order[destination_cup] = removed[0]

def simulate(order, num_moves, start_value):
    curr_value = start_value
    for curr_round in range(num_moves):
        removed = remove_elements(order, curr_value)
        destination_cup = determine_destination_cup(curr_value, removed)
        add_removed_at_destination(destination_cup, removed, order)
        curr_value = order[curr_value]

def find_one_neighbors(order):
    return [order["1"], order[order["1"]]]

def main():
    order_string = "974618352"
    order = create_mapping(order_string)
    num_rounds = 10000000
    simulate(order, num_rounds, order_string[0])
    neighbors = find_one_neighbors(order)
    print(int(neighbors[0]) * int(neighbors[1]))

main()
