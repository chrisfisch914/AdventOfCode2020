def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data = data.split("\n")[0]
    data = [int(elem) for elem in data.split(",")]
    return data

def main():
    input = fetch_input()
    seen = {}
    count = 1
    curr = input[0]
    rounds = 2020
    while(count < rounds):
        if curr in seen:
            old_count = seen[curr]
            seen[curr] = count
            curr = count - old_count
        else:
            seen[curr] = count
            if count < len(input):
                curr = input[count]
            else:
                curr = 0
        count += 1
    print(curr)

main()