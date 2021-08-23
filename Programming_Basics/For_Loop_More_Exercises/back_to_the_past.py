heritage_money = float(input())
year_of_living = int(input())

age = 17
spend_per_year = 0

for number in range(1800, year_of_living + 1):
    
    if number % 2 == 0:
        age += 1
        spend_per_year += 12000
        
    elif number % 2 == 1:
        age += 1
        spend_per_year += 12000 + (50 * age)
        
difference = heritage_money - spend_per_year

if difference >= 0:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
    
else:
    print(f"He will need {abs(difference):.2f} dollars to survive.")
