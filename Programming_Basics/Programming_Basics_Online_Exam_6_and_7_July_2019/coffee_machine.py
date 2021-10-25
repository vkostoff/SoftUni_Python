beverage = input()
sugar = input()
beverages_count = int(input())

price = 0

if beverage == "Espresso":
    
    if sugar == "Without":
        price += 0.9
        
    elif sugar == "Normal":
        price += 1
        
    elif sugar == "Extra":
        price += 1.2
        
elif beverage == "Cappuccino":
    
    if sugar == "Without":
        price += 1
        
    elif sugar == "Normal":
        price += 1.2
        
    elif sugar == "Extra":
        price += 1.6
        
elif beverage == "Tea":
    
    if sugar == "Without":
        price += 0.5
        
    elif sugar == "Normal":
        price += 0.6
        
    elif sugar == "Extra":
        price += 0.7
        
total_price = price * beverages_count

if sugar == "Without":
    total_price *= 0.65
    
if beverage == "Espresso" and beverages_count >= 5:
    total_price *= 0.75
    
if total_price > 15:
    total_price *= 0.80
    
print(f"You bought {beverages_count} cups of {beverage} for {total_price:.2f} lv.")
