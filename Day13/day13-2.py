from copy import deepcopy

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def inverse(ni, n):
    val = ni % n
    x = 1
    while (val * x) % n != 1:
        x += 1
    return x

# https://www.youtube.com/watch?v=zIFehsBHB8o
# Chinese remainder theorem
def crt(congruences):
    result = 0
    N = 1
    for bn in congruences:
        N *= bn[1]
    for bn in congruences:
        bi = bn[0]
        ni = N / bn[1]
        xi = inverse(ni, bn[1])
        result += bi * ni * xi
    return result % N

def convert_to_congruences(input):
    input = input.split(",")
    congruences = []
    for index, value in enumerate(input):
        if value != "x":
            congruences.append([int(value) - index, int(value)])
    return congruences

def main():
    input = fetch_input()
    congruences = convert_to_congruences(input[1])
    print(crt(congruences))

main()
