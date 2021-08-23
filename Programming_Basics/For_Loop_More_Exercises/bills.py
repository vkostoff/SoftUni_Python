months = int(input())

water_bill = 20
internet_bill = 15
other_bills = 0
total_electricity_bill = 0
total_other_bills = 0

for every_month in range(1, months + 1):
    electricity_bill = float(input())
    other_bills = (electricity_bill + 35) * 1.2
    total_other_bills += other_bills
    total_electricity_bill = total_electricity_bill + electricity_bill
    
total_water_bill = water_bill * months
total_internet_bill = internet_bill * months
average = (total_other_bills + total_water_bill + total_internet_bill + total_electricity_bill) / months

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")
