import re

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def parse_mask(mask_str):
    result = re.search('(X|\d)+', mask_str)
    return result.group(0)

def parse_mem_line(line):
    results = re.findall('\d+', line)
    return int(results[0]), int(results[1])

def set_bit(value, bit):
    return value | (1<<bit) 

def clear_bit(value, bit):
    return value & ~(1<<bit)

def apply_mask(mask, value):
    for index, mask_val in enumerate(mask):
        if mask_val == "1":
            value = set_bit(value, 35 - index)
        elif mask_val == "0":
            value = clear_bit(value, 35 - index)
    return value

def sum_values(memory):
    sum = 0
    for value in memory.values():
        sum += value
    return sum

def main():
    input = fetch_input()
    mask = ""
    memory = {}
    for line in input:
        if "mask" in line:
            mask = parse_mask(line)
        else:
            mem_address, value = parse_mem_line(line)
            memory[mem_address] = apply_mask(mask, value)
    print(sum_values(memory))

main()
