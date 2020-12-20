import re
import sys
sys.path.append("..")
from input_reader import InputReader

precedence = {
    "+": 1,
    "*": 1,
    "(": 0
}

def problem_to_tokens(problem):
    return [token for token in re.split(r'(\d+|\W)', problem) if token and token != " "]

def is_operator(char):
    return char == "+" or char == "*"

# http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
def shunting_yard(problem):
    tokens = problem_to_tokens(problem)
    op_stack = []
    result = []
    for token in tokens:
        if token == "(":
            op_stack.append(token)
        elif token == ")":
            curr = op_stack.pop()
            while curr != "(":
                result.append(curr)
                curr = op_stack.pop()
        elif is_operator(token) and (len(op_stack) == 0 or op_stack[-1] == "("):
            op_stack.append(token)
        elif is_operator(token) and precedence[token] > precedence[op_stack[-1]]:
            op_stack.append(token)
        elif is_operator(token):
            while len(op_stack) > 0 and precedence[token] <= precedence[op_stack[-1]]:
                result.append(op_stack.pop())
            op_stack.append(token)
        else:
            result.append(token)
    while len(op_stack) > 0:
        result.append(op_stack.pop())
    return result

def apply_operator(op, x, y):
    if op == "+":
        return int(x) + int(y)
    else:
        return int(x) * int(y)

def evaluate(problem):
    stack = []
    for value in problem:
        if is_operator(value):
            x = stack.pop()
            y = stack.pop()
            stack.append(apply_operator(value, x, y))
        else:
            stack.append(value)
    return stack.pop()

def main():
    final_result = 0
    problems = InputReader.fetch_input_lines()
    reworked_problems = [shunting_yard(problem) for problem in problems]
    results = [evaluate(problem) for problem in reworked_problems]
    print(sum(results))

main()