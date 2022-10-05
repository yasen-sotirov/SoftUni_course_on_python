length_of_aquarium = int(input())
with_of_aquarium = int(input())
height_of_aquarium = int(input())
percentage_ot_other = int(input()) / 100
volume_of_aquarium = (length_of_aquarium * with_of_aquarium * haight_of_aquarium) * 0.1
water = (volume_of_aquarium - (volume_of_aquarium * percentage_ot_other)) / 100
print(water)
