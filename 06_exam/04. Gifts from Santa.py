N_number = int(input())
M_number = int(input())
S_number = int(input())

for address in range(M_number, N_number, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == S_number:
            break
        print(address, end=' ')
