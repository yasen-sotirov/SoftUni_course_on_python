pool_volume = int(input())
capacity_pipe_1 = int(input())
capacity_pipe_2 = int(input())
hours = float(input())

water_from_pipe_1 = capacity_pipe_1 * hours
water_from_pipe_2 = capacity_pipe_2 * hours

total_water = water_from_pipe_1 + water_from_pipe_2
percentage_pipe_1 = water_from_pipe_1 / total_water * 100
percentage_pipe_2 = water_from_pipe_2 / total_water * 100
percentage_pool = total_water / pool_volume * 100

difference = abs(total_water - pool_volume)

if total_water <= pool_volume:
    print(f"The pool is {percentage_pool:.2f}% full. Pipe 1: {percentage_pipe_1:.2f}%. "
          f"Pipe 2: {percentage_pipe_2:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {difference:.2f} liters.")
