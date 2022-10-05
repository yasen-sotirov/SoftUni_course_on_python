amount_of_naelon = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
working_hours = int(input())
price_of_naelon = (amount_of_naelon + 2) * 1.50
price_of_paint = (amount_of_paint + amount_of_paint * 0.1) * 14.50
price_of_thinner = amount_of_thinner * 5.00
price_of_bags = 0.40
price_of_work = ((price_of_naelon + price_of_paint + price_of_thinner + price_of_bags) * 0.3)*working_hours
print(price_of_naelon + price_of_paint + price_of_thinner + price_of_bags + price_of_work)