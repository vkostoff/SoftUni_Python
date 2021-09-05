budget = float(input())
accommodations = int(input())
price_per_accommodation = float(input())
additional_expenses_percent = int(input())

if accommodations > 7:
    price_per_accommodation *= 0.95
    
additional_expenses = budget * (additional_expenses_percent / 100)
total_expenses = accommodations * price_per_accommodation + additional_expenses

if budget >= total_expenses:
    money_left = budget - total_expenses
    
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
    
else:
    money_needed = total_expenses - budget
    
    print(f"{money_needed:.2f} leva needed.")
