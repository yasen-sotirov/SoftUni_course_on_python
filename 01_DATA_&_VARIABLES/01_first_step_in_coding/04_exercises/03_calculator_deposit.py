# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit_amount = float(input())
months = int(input())
annual_interest_percent = float(input())
annual_interest = deposit_amount * annual_interest_percent / 100
monthly_interest = annual_interest / 12
total_sum = deposit_amount + months * monthly_interest
print(total_sum)