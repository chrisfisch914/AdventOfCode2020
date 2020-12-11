def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def get_first_second(first_second):
    first_second = first_second.split("-")
    min = int(first_second[0]) - 1
    max = int(first_second[1]) - 1
    return min, max

def is_valid_password(password):
    sections = password.split(' ')
    first, second = get_first_second(sections[0])
    needle = sections[1][0]
    haystack = sections[2]
    first_occur = haystack[first] == needle
    second_occur = haystack[second] == needle
    return (first_occur and not second_occur) or (not first_occur and second_occur)

def main():
    count = 0
    for line in fetch_input():
        if is_valid_password(line):
            count += 1
    print(count)

main()
