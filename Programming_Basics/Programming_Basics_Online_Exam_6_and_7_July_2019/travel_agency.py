destination = input()
package_type = input()
vip_discount = input()
days = int(input())

price_per_day = 0

if destination == "Bansko" or destination == "Borovets":
    
    if package_type == "withEquipment":
        price_per_day = 100
        
        if vip_discount == "yes":
            price_per_day *= 0.9
            
    elif package_type == "noEquipment":
        price_per_day = 80
        
        if vip_discount == "yes":
            price_per_day *= 0.95
            
elif destination == "Varna" or destination == "Burgas":
    
    if package_type == "withBreakfast":
        price_per_day = 130
        
        if vip_discount == "yes":
            price_per_day *= 0.88
            
    elif package_type == "noBreakfast":
        price_per_day = 100
        
        if vip_discount == "yes":
            price_per_day *= 0.93
            
total_price = days * price_per_day

if days > 7:
    total_price -= price_per_day
    
if days < 1:
    print("Days must be positive number!")
    
elif destination != "Bansko" and destination != "Borovets" and destination != "Varna" and destination != "Burgas":
    print("Invalid input!")
    
elif package_type != "noEquipment" and package_type != "withEquipment" and package_type != "noBreakfast"\
        and package_type != "withBreakfast":
    print("Invalid input!")
    
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
