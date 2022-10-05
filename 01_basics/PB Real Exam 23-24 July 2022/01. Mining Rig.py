from math import ceil

video_card_price = int(input())
connector_price = int(input())
electricity_price_per_day = float(input())
profit_per_day = float(input())

total_video_card_price = video_card_price * 13
total_connector_price = connector_price * 13
total_price_for_other_components = 1000

total_machine_price = total_video_card_price + total_connector_price + total_price_for_other_components
real_daily_profit = (profit_per_day - electricity_price_per_day) * 13

return_days = total_machine_price / real_daily_profit

print(total_machine_price)
print(ceil(return_days))
