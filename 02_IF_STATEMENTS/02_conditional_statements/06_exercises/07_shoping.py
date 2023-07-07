budget = float(input())
number_video_cards = int(input())
number_processor = int(input())
number_ram_memory = int(input())

price_video_cards = number_video_cards * 250
price_of_processors = price_video_cards * 0.35 * number_processor
price_of_ram_memory = price_video_cards * 0.1 * number_ram_memory

total_coast = price_video_cards + price_of_processors + price_of_ram_memory

if number_video_cards > number_processor:
    total_coast *= 0.85

difference = abs(budget - total_coast)

if budget >= total_coast:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
