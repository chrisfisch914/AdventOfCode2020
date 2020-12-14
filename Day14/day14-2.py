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

def get_bits(value, num_xs):
    result = []
    for i in range(num_xs):
        curr = (value & 1)
        result.append(curr)
        value >>= 1
    return [elem for elem in reversed(result)]

def apply_mask(mask, value):
    for index, mask_val in enumerate(mask):
        if mask_val == "1":
            value = set_bit(value, 35 - index)
    floating_addrs = []
    x_indexes = [m.start() for m in re.finditer('X', mask)]
    num_permuatations = pow(2, len(x_indexes))
    for i in range(num_permuatations):
        bits = get_bits(i, len(x_indexes))
        for bit_index, x_index in enumerate(x_indexes):
            bit = bits[bit_index]
            if bit == 1:
                value = set_bit(value, 35 - x_index)
            else:
                value = clear_bit(value, 35 - x_index)
        floating_addrs.append(value)
    return floating_addrs

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
            new_addresses = apply_mask(mask, mem_address)
            for new_address in new_addresses:
                memory[new_address] = value
    print(sum_values(memory))

main()
