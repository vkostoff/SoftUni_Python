budget = float(input())
serials = int(input())

money_spent = 0

for serials in range(1, serials + 1):
    serial_name = input()
    serial_price = float(input())
    
    if serial_name == "Thrones":
        serial_price *= 0.5
        money_spent += serial_price
        
    elif serial_name == "Lucifer":
        serial_price *= 0.6
        money_spent += serial_price
        
    elif serial_name == "Protector":
        serial_price *= 0.7
        money_spent += serial_price
        
    elif serial_name == "TotalDrama":
        serial_price *= 0.8
        money_spent += serial_price
        
    elif serial_name == "Area":
        serial_price *= 0.9
        money_spent += serial_price
        
    else:
        money_spent += serial_price
        
if money_spent > budget:
    money_needed = money_spent - budget
    print(f"You need {money_needed:.2f} lv. more to buy the series!")
    
else:
    money_left = budget - money_spent
    print(f"You bought all the series and left with {money_left:.2f} lv.")
