def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data = data.split("\n")
    input = []
    curr = ""
    for line in data:
        if len(line) == 0:
            input.append(curr)
            curr = ""
        else:
            curr += " "
            curr += line
    input.append(curr)
    return input

def fetch_keys(key_values):
    return [pair.split(":")[0] for pair in key_values]

def main():
    input = fetch_input()
    values_to_verify = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    count = 0
    for line in input:
        key_values = line.split(" ")
        keys = fetch_keys(key_values)
        if values_to_verify.issubset(set(keys)):
            count += 1
    print(count)

main()
