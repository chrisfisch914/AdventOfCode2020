def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data =  data.split("\n")
    return [int(elem) for elem in data]

def main():
    input = fetch_input()
    input.sort(reverse=True)
    result_length = len(input) + 1
    result = [0 for i in range(result_length)]
    result[0] = 1 # the largest value is always 3 away from our device 
    for index, value in enumerate(input):
        for i in range(1, 4):
            if index - i >= 0 and input[index - i] - value <= 3:
                result[index] += result[index - i]
    for i in range(1, 4):
            if input[result_length - 1 - i]  <= 3:
                result[result_length - 1] += result[result_length - 1 - i]
    print(result[result_length - 1])

main()