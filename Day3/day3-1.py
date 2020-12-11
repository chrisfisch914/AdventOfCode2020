def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def main():
    input = fetch_input()
    line_length = len(input[0])
    count = 0
    index = 0
    for line in input:
        if line[index] == '#':
            count += 1
        index = (index + 3) % line_length
    print(count)

main()
