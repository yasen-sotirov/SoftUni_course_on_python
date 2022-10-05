number_package_pencil = int(input())
number_package_marker = int(input())
number_liters_of_cleaning_solution = int(input())
discount = int(input())
price_all_pencil = number_package_pencil * 5.80
price_all_marker = number_package_marker * 7.20
price_all_liters_cleaning_solution = number_liters_of_cleaning_solution * 1.20
percentage_discount = discount / 100
total_price = price_all_pencil + price_all_marker + price_all_liters_cleaning_solution
total_price_with_discount = total_price - (total_price * percentage_discount)
print(total_price_with_discount)