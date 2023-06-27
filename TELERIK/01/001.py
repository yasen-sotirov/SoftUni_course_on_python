def add_number(a, b, c=3):
    if not c:
        return a + b
    else:
        return a + b + c


result = add_number(2, b=4, c=4)
print(result)
