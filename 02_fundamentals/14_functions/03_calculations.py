"""" Create a function that receives three parameters, calculates
a result depending on the given operator, and returns it.
Print the result of the function.
The input comes as three parameters – an operator as a string
and two integer numbers. The operator can be one of the following:
"multiply", "divide", "add", "subtract".
"""


def calculations(operator, num_1, num_2):
    result = None
    if operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = int(num_1 / num_2)     #става и с  //
    elif operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    return result


operator_sing = input()
number_1 = int(input())
number_2 = int(input())
print(calculations(operator_sing, number_1, number_2))