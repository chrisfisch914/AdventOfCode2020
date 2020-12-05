def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def get_max_min(max_min):
    max_and_min = max_min.split("-")
    min = int(max_and_min[0])
    max = int(max_and_min[1])
    return min, max

def is_valid_password(password):
    sections = password.split(' ')
    min, max = get_max_min(sections[0])
    needle = sections[1][0]
    haystack = sections[2]
    occurances = haystack.count(needle)
    return occurances >= min and occurances <= max

def main():
    count = 0
    for line in fetch_input():
        if is_valid_password(line):
            count += 1
    print(count)

main()