number = int(input())
merged_nums = []
squashed_nums = []
sequence = []

for _ in range(number):
    current_num = int(input())
    sequence.append(current_num)

for index in range(number - 1):
    first_num = sequence[index]
    second_num = sequence[index + 1]

    first_num_as_str = [x for x in str(first_num)]
    second_num_as_str = [x for x in str(second_num)]

    merging = first_num_as_str[1] + second_num_as_str[0]
    merged_nums.append(merging)

    middle_squashed = int(first_num_as_str[1]) + int(second_num_as_str[0])
    if middle_squashed > 9:
        middle_squashed = [x for x in str(middle_squashed)][1]

    squashing = first_num_as_str[0] + str(middle_squashed) + second_num_as_str[1]
    squashed_nums.append(squashing)

print(' '.join(merged_nums))
print(' '.join(squashed_nums))

