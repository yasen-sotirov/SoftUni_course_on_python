number_one = int(input())
number_two = int(input())
operator = input()

result = 0
odd_or_even = ""

if operator == "+":
    result = number_one + number_two
    if result % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {odd_or_even}")
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {odd_or_even}")
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {odd_or_even}")
elif operator == "/":
    if number_two != 0:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")
    else:
        print(f"Cannot divide {number_one} by zero")
elif operator == "%":
    if number_two != 0:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")
    else:
        print(f"Cannot divide {number_one} by zero")
