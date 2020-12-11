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

def can_contain(data, curr_key, to_find):
    if curr_key == to_find:
        return True
    if (len(data[curr_key]) == 0):
        return False
    result = False
    for bag in data[curr_key]:
        result |= can_contain(data, bag["color"], to_find)
    return result
    

def search_for_color(data, to_find):
    print(data)
    count = 0
    for key in data.keys():
        if key != to_find and  can_contain(data, key, to_find):
            count += 1
    print(count)

def main():
    input = fetch_input()
    data = parse_input_to_map(input)
    results = search_for_color(data, "shiny gold")

main()
