import re
import sys
sys.path.append("..")
from input_reader import InputReader

SUBJECT_NUMBER = 7
DIVISOR = 20201227

def calculate_loop_size(key):
    value = 1
    loop_size = 0
    while value != key:
        loop_size += 1
        value *= SUBJECT_NUMBER
        value %= DIVISOR
    return loop_size

def calculate_encryption_key(loop_size, public_key):
    value = 1
    for _ in range(loop_size):
        value *= public_key
        value %= DIVISOR
    return value

def main():
    [card_public_key, door_public_key] = InputReader.fetch_numbers()
    card_loop_size = calculate_loop_size(card_public_key)
    door_loop_size = calculate_loop_size(door_public_key)
    print(calculate_encryption_key(card_loop_size, door_public_key))
    print(calculate_encryption_key(door_loop_size, card_public_key))


main()
