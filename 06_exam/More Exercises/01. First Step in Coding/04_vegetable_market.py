price_per_kg_vegetables = float(input())
price_per_kg_fruit = float(input())
total_volume_vegetables = int(input())
total_volume_fruits = int(input())

total_income_bgn = total_volume_vegetables * price_per_kg_vegetables + total_volume_fruits * price_per_kg_fruit
euro_converter = total_income_bgn / 1.94

print(f'{euro_converter:.2f}')
