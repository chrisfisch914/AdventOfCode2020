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

def find_irregular_value(data):
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
            return to_find

def find_contiguous_subarray_sum(to_find, data):
    running_sum = 0
    subarray = []
    index_to_remove = 0
    for value in data:
        subarray.append(value)
        running_sum += value
        while running_sum > to_find:
            running_sum -= subarray[index_to_remove]
            index_to_remove += 1
        if running_sum == to_find:
            return subarray[index_to_remove:]

def main():
    data = fetch_input()
    bad_value = find_irregular_value(data)
    subarray = find_contiguous_subarray_sum(bad_value, data)
    subarray.sort()
    print(subarray[0] + subarray[len(subarray) - 1])

main()
