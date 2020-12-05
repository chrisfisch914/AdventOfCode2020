def fetch_input():
    data = ''
    with open('input.txt', 'r') as file:
        data = file.read()
    input = data.split("\n")
    return [int(elem) for elem in input]

def main():
    input = fetch_input()
    cache = {}
    for elem in input:
        if elem in cache:
            match = cache[elem]
            print(elem * match)
        cache[2020 - elem] = elem

main()