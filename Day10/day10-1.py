def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data =  data.split("\n")
    return [int(elem) for elem in data]

def main():
    input = fetch_input()
    input.sort()
    result = {1: 0, 2: 0, 3: 0}
    curr = 0
    for value in input:
        dist = value - curr
        result[dist] += 1
        curr = value
    result[3] += 1
    print(result[1] * result[3])

main()