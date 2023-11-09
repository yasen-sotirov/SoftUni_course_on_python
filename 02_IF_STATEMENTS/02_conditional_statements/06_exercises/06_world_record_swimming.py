old_record = float(input())
distance = float(input())
time_for_one_meter = float(input())
delay = (distance // 15) * 12.5
sum_time = (distance * time_for_one_meter) + delay

if sum_time < old_record:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
else:
    seconds = sum_time - old_record
    print(f"No, he failed! He was {seconds:.2f} seconds slower.")
