def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    groups =  data.split("\n\n")
    for i in range(len(groups)):
        groups[i] = groups[i].split("\n")
    return groups

def main():
    groups = fetch_input()
    count = 0
    for group in groups:
        seen = set()
        for person in group:
            for index in range(len(person)):
                seen.add(person[index])
        count += len(seen)
    print(count)

main()
