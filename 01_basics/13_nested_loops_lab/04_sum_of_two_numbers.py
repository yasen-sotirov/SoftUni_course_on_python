start_number = int(input())
final_number = int(input())
magic_number = int(input())

combination = 0
flag = False

for num1 in range(start_number, final_number + 1):
    for num2 in range(start_number, final_number + 1):
        combination += 1

        if num1 + num2 == magic_number:
            flag = True
            print(f"Combination N:{combination} ({num1} + {num2} = {magic_number})")
            break
    if flag:
        break

if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")
