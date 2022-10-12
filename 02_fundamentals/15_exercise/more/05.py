def is_negative(n_1, n_2, n_3):
    if n_1 < 0 or n_2 < 0 or n_3 < 0:
        return 'negative'
    return 'positive'


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(is_negative(num_1, num_2, num_3))
