import re

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

# this function is necessary because of pythons lazy execution
def create_lambda(b1, b2, b3, b4):
    return lambda x : b1 <= x <= b2 or b3 <= x <= b4

def parse_fields_to_functions(input):
    field_to_function = {}
    index = 0
    while input[index] != "":
        field = re.search("[a-z]+(\s|[a-z])+", input[index]).group(0)
        bounds = re.findall("\d+", input[index])
        bounds = [int(bound) for bound in bounds]
        field_to_function[field] = create_lambda(bounds[0], bounds[1], bounds[2], bounds[3])
        index += 1
    return index, field_to_function

def value_is_valid(value, field_to_function):
    for key in field_to_function:
        if field_to_function[key](value):
            return True
    return False

def ticket_is_valid(ticket, field_to_function):
    for field in ticket.split(","):
        field = int(field)
        if not value_is_valid(field, field_to_function):
            return False
    return True

def remove_invalid_tickets(tickets, field_to_function):
    return [ticket for ticket in tickets if ticket_is_valid(ticket, field_to_function)]

def process_of_elimination(potential_name_per_column):
    done = False
    while not done:
        column_finished_count = 0
        for curr_index, column_set in enumerate(potential_name_per_column):
            if len(column_set) == 1:
                column_finished_count += 1
                for other_index, other_column_set in enumerate(potential_name_per_column):
                    if curr_index != other_index:
                        potential_name_per_column[other_index] = other_column_set.difference(column_set)
        done = column_finished_count == len(potential_name_per_column)
    column_names = [list(column_set)[0] for column_set in potential_name_per_column]
    return column_names

def determine_column_names(nearby_tickets, field_to_function):
    num_columns = len(field_to_function)
    potential_name_per_column = []
    for _ in range(num_columns):
        potential_name_per_column.append(set(field_to_function.keys()))
    for ticket in nearby_tickets:
        for value_index, value in enumerate(ticket.split(",")):
            value = int(value)
            keys_to_remove = set()
            for key in potential_name_per_column[value_index]:
                if not field_to_function[key](value):
                    keys_to_remove.add(key)
            potential_name_per_column[value_index] = potential_name_per_column[value_index].difference(keys_to_remove)
    return process_of_elimination(potential_name_per_column)

def mutiply_depature_fields(my_ticket, column_names):
    result = 1
    for index, column_name in enumerate(column_names):
        if "departure" in column_name:
            result *= my_ticket[index]
    return result

def main():
    input = fetch_input()
    index_reached, field_to_function = parse_fields_to_functions(input)
    my_ticket = input[index_reached + 2 : index_reached + 3][0]
    my_ticket = [int(value) for value in my_ticket.split(",")]
    nearby_tickets = input[index_reached + 5:] # skip ahead to nearby tickets
    valid_nearby_tickets = remove_invalid_tickets(nearby_tickets, field_to_function)
    column_names = determine_column_names(valid_nearby_tickets, field_to_function)
    print(mutiply_depature_fields(my_ticket, column_names))

main()
