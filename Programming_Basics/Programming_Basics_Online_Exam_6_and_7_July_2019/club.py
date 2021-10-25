desired_profit = float(input())

income = 0

command = input()

while command != "Party!":
    cocktail_name = command
    cocktails_count = int(input())
    current_income = cocktails_count * len(cocktail_name)
    
    if current_income % 2 == 1:
        income += (current_income * 0.75)
        
    else:
        income += current_income
        
    if income >= desired_profit:
        print("Target acquired.")
        break
        
    command = input()
    
if income < desired_profit:
    money_needed = desired_profit - income
    
    print(f"We need {money_needed:.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")
    
else:
    print(f"Club income - {income:.2f} leva.")
