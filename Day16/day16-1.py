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

def count_invalid_numbers(input, field_to_function):
    count = 0
    for line in input:
        for value in line.split(","):
            value = int(value)
            if not value_is_valid(value, field_to_function):
                count += value
    return count

def main():
    input = fetch_input()
    index_reached, field_to_function = parse_fields_to_functions(input)
    input = input[index_reached + 5:] # skip ahead to nearby tickets
    print(count_invalid_numbers(input, field_to_function))

main()
