""" 8.	Age Assignment
Create a function called age_assignment() that receives a different number of
names and a different number of key-value pairs. The key will be a single letter
(the first letter of each name) and the value - a number (age).
Find its first letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return
the information for each person on a new line in the format: "{name} is {age} years old."
Submit only the function in the judge system.

Examples
    Test Code
print(age_assignment("Peter", "George", G=26, P=19))

    Output
George is 26 years old.
Peter is 19 years old.

"""


def age_assignment(*args, **kwargs):
    name_list = {}

    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                name_list[name] = value

    result = ""
    for name, age in sorted(name_list.items()):
        result += f"{name} is {age} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
 