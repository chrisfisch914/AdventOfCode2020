import re

def fetch_input():
    data = []
    with open('input.txt', 'r') as file:
        data = file.read()
    data = data.split("\n")
    input = []
    curr = ""
    for line in data:
        if len(line) == 0:
            input.append(curr.strip())
            curr = ""
        else:
            curr += " "
            curr += line
    input.append(curr.strip())
    return input

def passport_to_dictionary(key_values):
    result = {}
    for pair in key_values:
        key_value = pair.split(":")
        key =  key_value[0]
        value = key_value[1]
        result[key] = value
    return result

def validate_keys(data):
    values_to_verify = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    keys = set(data.keys())
    return values_to_verify.issubset(keys)

def validate_is_four_digits(input):
    match = re.search("^\d{4}$", input)
    return match is not None

def value_between(value, min, max):
    value = int(value)
    return value >= min and value <= max

def valid_birth_year(value):
    return validate_is_four_digits(value) and value_between(value, 1920, 2002)

def valid_issue_year(value):
    return validate_is_four_digits(value) and value_between(value, 2010, 2020)

def valid_expr_year(value):
    return validate_is_four_digits(value) and value_between(value, 2020, 2030)

def valid_height(height):
    match = re.search("^\d+(cm|in)$", height)
    if match is None:
        return False
    if "cm" in height:
        value = height.split("cm")[0]
        return value_between(value, 150, 193)
    else:
        value = height.split("in")[0]
        return value_between(value, 59, 76)

def valid_hair_color(haircolor):
    match = re.search("^#[0-9a-f]{6}$", haircolor)
    return match is not None

def valid_eye_color(eyecolor):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eyecolor in valid_colors

def valid_passport_id(pid):
    match = re.search("^\d{9}$", pid)
    return match is not None

def valid_country_id(value):
    return True

def is_valid_dictionary(data):
    field_to_func = {
        "byr": valid_birth_year,
        "iyr": valid_issue_year,
        "eyr": valid_expr_year,
        "hgt": valid_height,
        "hcl": valid_hair_color,
        "ecl": valid_eye_color,
        "pid": valid_passport_id,
        "cid": valid_country_id
    }
    if not validate_keys(data):
        return False
    for key in data.keys():
        if not field_to_func[key](data[key]):
            return False
    return True

def is_valid_passport(passport):
    key_values = passport.split(" ")
    data = passport_to_dictionary(key_values)
    return is_valid_dictionary(data)


def main():
    input = fetch_input()
    count = 0
    for line in input:
        if is_valid_passport(line):
            count += 1
    print(count)

main()
