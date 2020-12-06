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
        seen = {}
        for person in group:
            for index in range(len(person)):
                if person[index] in seen:
                    seen[person[index]] += 1
                else:
                    seen[person[index]] = 1
        group_size = len(group)
        for key in seen.keys():
            if seen[key] == group_size:
                count += 1
    print(count)

main()