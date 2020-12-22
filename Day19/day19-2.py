import regex
import sys
sys.path.append("..")
from input_reader import InputReader

def seperate_rules_from_words(rules_and_words):
    rules = [rule for rule in rules_and_words if ":" in rule]
    words = [word for word in rules_and_words if not ":" in word and word != ""]
    return rules, words

def format_rules(rules):
    formatted_rules = {}
    for rule in rules:
        splits = rule.split(":")
        formatted_rules[splits[0]] = splits[1].strip()
    return formatted_rules

def build_regex(rules, key, memo):
    if key in memo:
        return memo[key]
    if "\"" in rules[key]:
        return rules[key][1: len(rules[key]) - 1]
    result = ""
    add_parens = False
    for new_key in rules[key].split(" "):
        if new_key == "|":
            result += "|"
            add_parens = True
        else:
            blah = build_regex(rules, new_key, memo)
            result += build_regex(rules, new_key, memo)
    if add_parens:
            result = "(" + result + ")"
    memo[key] = result
    return memo[key]


def main():
    rules_and_words = InputReader.fetch_input_lines()
    rules, words = seperate_rules_from_words(rules_and_words)
    rules = format_rules(rules)
    mem_42 = build_regex(rules, "42", {})
    mem_31 = build_regex(rules, "31", {})
    solution_set = set()
    max_word_size = 0
    for word in words:
        max_word_size = max(max_word_size, len(word))
    for x in range(1, max_word_size):
        memo = {}
        memo["8"] = mem_42 + "+"
        memo["11"] = "(" + mem_42 + "){" + str(x) + "}" + "(" + mem_31 + "){" + str(x) + "}"
        sol = "^" + build_regex(rules, "0", memo) + "$"
        results = [word for word in words if regex.match(sol, word)]
        for result in results:
            solution_set.add(result)
    for blah in solution_set:
        print(blah)
    print(len(solution_set))

main()
