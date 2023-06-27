number = int(input())
nums_dict = {}
sorted_dict = {0: 0}

most_resent_num = 0
count_most_resent_num = 0

for _ in range(number):
    current_num = int(input())
    if current_num not in nums_dict:
        nums_dict[current_num] = 0
    nums_dict[current_num] += 1


for key, value in nums_dict.items():
    if value > count_most_resent_num:
        count_most_resent_num = value
        most_resent_num = key

print(most_resent_num)
 