number_of_days = int(input())
doctors = 7
counter_day = 0
total_treated_patient = 0
total_untreated_patient = 0


for i in range(1, number_of_days + 1):
    counter_day += 1
    arrived_patients = int(input())
    if counter_day % 3 == 0:
        if total_untreated_patient > total_treated_patient:
            doctors += 1
    if arrived_patients > doctors:
        total_untreated_patient += arrived_patients - doctors
        total_treated_patient += doctors
    else:
        total_treated_patient += arrived_patients

print(f"Treated patients: {total_treated_patient}.")
print(f"Untreated patients: {total_untreated_patient}.")
