""" 5.	Concatenate
Write a concatenate() function that receives some strings as arguments and some named arguments
(the key will be a string, and the value will be another string).
First, you should concatenate all arguments successively.
Next, take each key successively, and if it is present in the resulted string,
change all matching parts with the key's value. In the end, return the final string.

See the examples for more clarification.
Submit only your function in the judge system.

Examples
Test Code
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
Output
SoftUniIsGreat!
"""


def concatenate(*args, **kwargs):
    main_string = ''.join(args)

    for key, value in kwargs.items():
        if key in main_string:
            main_string = main_string.replace(key, value)
    return main_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
