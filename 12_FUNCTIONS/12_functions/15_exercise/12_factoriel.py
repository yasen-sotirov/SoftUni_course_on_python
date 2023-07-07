"""" Write a function that receives two integer numbers.
Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
"""


def factoriel(number_1, number_2):
    factoriel_1 = 1
    factoriel_2 = 1

    for factor_1 in range(num_1, 1, -1):
        factoriel_1 *= factor_1
    for factor_2 in range(num_2, 1, -1):
        factoriel_2 *= factor_2
    return f"{factoriel_1 / factoriel_2:.2f}"


num_1, num_2 = int(input()), int(input())
print(factoriel(num_1, num_2))

