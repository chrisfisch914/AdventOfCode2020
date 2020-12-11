def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def parse_input_to_map(input):
    result = {}
    for line in input:
        fields = line.split("contain ")
        key_values = fields[0].split(" ")
        key = key_values[0] + " " + key_values[1]
        value = []
        if not "no other bags" in fields[1]:
            bags = fields[1].split(", ")
            for bag in bags:
                words = bag.split(" ")
                count = int(words[0])
                color = words[1] + " " + words[2]
                value.append({"count": count, "color": color})
        result[key] = value
    return result

def count_for_color(data, to_find):
    count = 0
    if len(data[to_find]) == 0:
        return 0
    for bag in data[to_find]:
        count += bag["count"] * (count_for_color(data, bag["color"]) + 1)
    return count

def main():
    input = fetch_input()
    data = parse_input_to_map(input)
    result = count_for_color(data, "shiny gold")
    print(result)

main()
