days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for period in range(1, days + 1):
    daily_patients = int(input())
    if period % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if daily_patients <= doctors:
        treated_patients += daily_patients
    else:
        treated_patients += doctors
        untreated_patients += (daily_patients - doctors)
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')