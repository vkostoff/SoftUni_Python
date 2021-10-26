contract_duration = input()
contract_type = input()
mobile_data = input()
months_count = int(input())

monthly = 0

if contract_type == "Small":
    
    if contract_duration == "one":
        monthly = 9.98
    elif contract_duration == "two":
        monthly = 8.58
        
elif contract_type == "Middle":
    
    if contract_duration == "one":
        monthly = 18.99
    elif contract_duration == "two":
        monthly = 17.09
        
elif contract_type == "Large":
    
    if contract_duration == "one":
        monthly = 25.98
    elif contract_duration == "two":
        monthly = 23.59
        
elif contract_type == "ExtraLarge":
    
    if contract_duration == "one":
        monthly = 35.99
    elif contract_duration == "two":
        monthly = 31.79
        
if mobile_data == "yes":
    
    if monthly <= 10:
        monthly += 5.5
    elif 10 < monthly <= 30:
        monthly += 4.35
    elif monthly > 30:
        monthly += 3.85
        
total_spent = monthly * months_count

if contract_duration == "two":
    total_spent *= 0.9625
    
print(f"{total_spent:.2f} lv.")
