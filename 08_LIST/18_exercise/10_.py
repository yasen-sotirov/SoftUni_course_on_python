"""" You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
•	You must increase the value of all elements in the sequence which are less or equal to the removed element with the value of the removed element.
•	You must decrease the value of all elements in the sequence which are greater than the removed element with the value of the removed element.
If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
Input
•	On the first line of input, you will receive a sequence of integers, separated by spaces.
•	On the next several lines, you will receive integers - the indexes.
Output
•	When the program ends, you must print the summed value of all removed elements.
Constrains
•	The input data will consist only of valid integers in the range [-2.147.483.648…2.147.483.647].
"""

# https://github.com/ceo-py/softuni/blob/main/Python-Fundamentals/Lists%20Advanced%20-%20Exercise/13_pokemon_dont_go.py



data = input().split()
list_of_pokemons = [int(num) for num in data]
sum_of_removed = 0

while len(list_of_pokemons) > 0:
    index = int(input())

    if index < 0:
        list_of_pokemons[0] = list_of_pokemons[-1]
    elif index > len(list_of_pokemons) -1:
        list_of_pokemons[-1] = list_of_pokemons[0]
    else:
        del list_of_pokemons[index]
        sum_of_removed += list_of_pokemons[index]
        for element in list_of_pokemons:
            if element <= index:
                element += index
            else:
                element -= index

print(sum_of_removed)