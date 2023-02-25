from functools import reduce


def operate(sign, *args):
    try:
        return reduce(lambda x, y: eval(f"{x} {sign} {y}"), args)
    # изчистваме нулите, или хвърляме грешка
    except ZeroDivisionError:
        return reduce(lambda x, y: eval(f"{x} {sign} {y}"), [el for el in args if el != 0])

# def operate(operator, *args):
#     result = args[0]
#
#     if operator == "+":
#         result = sum(args)
#
#     elif operator == "_":
#         for x in args[1:]:
#             result -= x
#
#     elif operator == "*":
#         for x in args[1:]:
#             result *= x
#
#     elif operator == "/":
#         for x in args[1:]:
#             result /= x
#
#     return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
