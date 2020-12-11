def fetch_input():
    data = ''
    with open('input.txt', 'r') as file:
        data = file.read()
    input = data.split("\n")
    return [int(elem) for elem in input]

def main():
    input = fetch_input()
    for i in range(len(input)):
        cache = {}
        to_find = 2020 - input[i]
        for j in range(i + 1, len(input)):
            if input[j] in cache:
                match = cache[input[j]]
                print(input[i] * input[j] * match)
            cache[to_find - input[j]] = input[j] 

main()
