square_meter_of_yard = float(input())
price_for_landscaping_the_thole_yard = square_meter_of_yard * 7.61
calculated_discount = price_for_landscaping_the_thole_yard * 0.18
final_price = price_for_landscaping_the_thole_yard - calculated_discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {calculated_discount} lv.")
