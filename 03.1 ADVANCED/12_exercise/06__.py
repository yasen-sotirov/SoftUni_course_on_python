""" 6.	Function Executor
Create a function called func_executor() that can receive a different number of tuples,
each of which will have exactly 2 elements: the first will be a function,
and the second will be a tuple of the arguments that need to be passed to that function.
You should execute each function and return its result in the format:
"{function name} - {function result}"

For more clarification, see the examples below.
Submit only your function in the judge system.

    Examples
    Test Code

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))

    Output

sum_numbers - 3
multiply_numbers - 8

"""


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = {}
    for func_name, func_params in args:
        func_ref = func_name(*func_params)
        result[func_name] = func_ref

    for key, value in result.items():
        print(f"{key} - {value}")


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
