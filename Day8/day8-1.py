def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    return data.split("\n")

def decipher_command(line):
    split_line = line.split(" ")
    cmd = {"action": split_line[0], "value": int(split_line[1])}
    return cmd

def detect_cycle(input):
    acc = 0
    index = 0
    seen_indexes = set()
    cycle_detected = False
    while (index < len(input)):
        if index in seen_indexes:
            cycle_detected = True
            break
        seen_indexes.add(index)
        line = input[index]
        cmd = decipher_command(line)
        if cmd["action"]  == "acc":
            acc += cmd["value"]
        if cmd["action"] == "jmp":
            index += cmd["value"]
        else:
            index += 1
        last_seen = line
    return cycle_detected, acc


def main():
    input = fetch_input()
    _, acc = detect_cycle(input)
    print(acc)
main()