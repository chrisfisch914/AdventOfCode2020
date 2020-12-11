def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data =  data.split("\n")
    return [int(elem) for elem in data]

def find(values, to_find):
    for value in values:
        if to_find - value in values:
            return True
    return False

def main():
    data = fetch_input()
    preamble_size = 25
    preamble = data[0:preamble_size]
    remaining = data[preamble_size:]
    index_to_remove = 0
    values = set(preamble)
    for to_find in remaining:
        if find(values, to_find):
            values.remove(data[index_to_remove])
            values.add(to_find)
            index_to_remove += 1
        else:
            print(to_find)
            break
main()
