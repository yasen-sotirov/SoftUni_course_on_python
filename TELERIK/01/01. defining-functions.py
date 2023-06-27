# comments are here for guidance
# you can delete them before the demo

# 1
# ideal functions have input and output (parameters and return)
def greet(name):
    message = f'Hello, {name}'
    return message


# you can store the result in a variable
greeting = greet('Pesho')
print(greeting)

# or pass it to another function
print(greet('Gosho'))

# 2
# functions can be without parameters and/or return


def print_some_greeting():
    print('Hello, random dude!')


# you can't pass any values to the function
print_some_greeting()
print_some_greeting()

# a function without return statement actually returns None
returned_value = print_some_greeting()
print(f'Function without return actually returns {returned_value}')
