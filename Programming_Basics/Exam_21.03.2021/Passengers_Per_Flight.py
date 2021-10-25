from math import floor
best_aircompany = ""
best_passengers = 0
aircompanies = int(input())
for aircompanies in range(1, aircompanies + 1):
    aircompany_name = input()
    total_passengers = 0
    counter = 0
    command = input()
    while command != "Finish":
        passengers = int(command)
        total_passengers += passengers
        counter += 1
        command = input()
    average_passengers = total_passengers / counter
    print(f"{aircompany_name}: {floor(average_passengers)} passengers.")
    if average_passengers > best_passengers:
        best_passengers = floor(average_passengers)
        best_aircompany = aircompany_name
print(f"{best_aircompany} has most passengers per flight: {best_passengers}")