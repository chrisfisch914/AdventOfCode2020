def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def calculate_for_slope(input, right, down):
    line_length = len(input[0])
    count = 0
    column = 0
    for index in range(0, len(input), down):
        line = input[index]
        if line[column] == '#':
            count += 1
        column = (column + right) % line_length
    return count
        

def main():
    input = fetch_input()
    first = calculate_for_slope(input, 1, 1)
    second = calculate_for_slope(input, 3, 1)
    third = calculate_for_slope(input, 5, 1)
    fourth = calculate_for_slope(input, 7, 1)
    fifth = calculate_for_slope(input, 1, 2)
    print(first * second * third * fourth * fifth)

main()
