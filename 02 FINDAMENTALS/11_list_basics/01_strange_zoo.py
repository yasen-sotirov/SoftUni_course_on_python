""" You are at the zoo, and the meerkats look strange.
You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. Your task is to re-arrange the elements in a list so that the animal looks normal again:
•	On the first position is the head;
•	On the second position is the body;
•	On the last one is the tail.
"""


my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]    #slap -ване: смяна на местата в листа

print(my_list)
