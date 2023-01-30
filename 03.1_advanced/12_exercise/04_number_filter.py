""" 4.	Numbers Filter
Create a function called even_odd_filter() that can receive a different number of named arguments.
The keys will be "even" and/or "odd", and the values will be a list of numbers.
When the key is "odd", you should extract only the odd numbers from its list.
When the key is "even", you should extract only the even numbers from its list.
The function should return a dictionary sorted by the length of the lists in descending order.
There will be no case of lists with the same length.
Submit only your function in the judge system.

    Example
    Input
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

    Output
{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
"""


def even_odd_filter(**kwargs):
    result = {}
    for number_type, number in kwargs.items():
        if number_type == "even":
            result[number_type] = [x for x in number if x % 2 == 0]
        else:
            result[number_type] = [x for x in number if x % 2 != 0]
    return dict(sorted(result.items()))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
