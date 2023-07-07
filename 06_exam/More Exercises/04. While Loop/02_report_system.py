charity_goal = int(input())
charity_goal_is_reached = False
command = input()
collected_sum = 0
transaction_counter = 0

people_paid_by_cash = 0
sum_paid_by_cash = 0

people_paid_by_card = 0
sum_paid_by_card = 0

while command != 'End':
    income = int(command)
    transaction_counter += 1

    if transaction_counter % 2 != 0:
        if income <= 100:
            collected_sum += income
            people_paid_by_cash += 1
            sum_paid_by_cash += income
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if income > 10:
            collected_sum += income
            people_paid_by_card += 1
            sum_paid_by_card += income
            print("Product sold!")
        else:
            print("Error in transaction!")

    if collected_sum >= charity_goal:
        charity_goal_is_reached = True
        break
    command = input()

if collected_sum >= charity_goal:
    print(f"Average CS: {sum_paid_by_cash / people_paid_by_cash:.2f}")
    print(f"Average CC: {sum_paid_by_card / people_paid_by_card:.2f}")
else:
    print("Failed to collect required money for charity.")
