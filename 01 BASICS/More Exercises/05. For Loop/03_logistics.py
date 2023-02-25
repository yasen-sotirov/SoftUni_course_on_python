number_of_loads = int(input())
counter_bus = 0
counter_truck = 0
counter_train = 0
counter_weight = 0
total_price = 0

for i in range(number_of_loads):
    weight_of_load = int(input())
    counter_weight += weight_of_load
    if weight_of_load <= 3:
        counter_bus += weight_of_load
        total_price += weight_of_load * 200
    elif weight_of_load <= 11:
        counter_truck += weight_of_load
        total_price += weight_of_load * 175
    else:
        counter_train += weight_of_load
        total_price += weight_of_load * 120

average_price = total_price / counter_weight
percentage_bus = counter_bus / counter_weight * 100
percentage_truck = counter_truck / counter_weight * 100
percentage_train = counter_train / counter_weight * 100

print(f'{average_price:.2f}')
print(f'{percentage_bus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')
