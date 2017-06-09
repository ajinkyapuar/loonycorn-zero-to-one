# Simple command line calculator (11 - 2 + 3 * 4 / 5) -> no precedence; will evaluate as it reads.
# Assume all numbers will be positive integers and there will be 1 space between an operator and operand.
# Also assume experssions are always going to be valid. YOu dont have to account for edge cases.
# And it will only have `-, +, *, /` operators

from operator import add, sub, mul, truediv

operator_dict = {
    '+': add,
    '-': sub,
    '/': truediv,
    '*': mul,
}


def calc(expr):
    tokens = expr.split()
    numbers = [int(i) for i in tokens if i.isdigit()]
    operators = [i for i in tokens if not i.isdigit()]
    result = numbers[0]
    for operator, value in zip(operators, numbers[1:]):
        result = operator_dict[operator](result, value)
    return result


print(calc("8 + 2 - 3 / 4 * 3"))
