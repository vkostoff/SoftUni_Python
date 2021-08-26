fruit = input()
size = input()
ordered = int(input())

price = 0

if fruit == "Watermelon":
    
    if size == "small":
        price = 56 * 2
        
    elif size == "big":
        price = 28.70 * 5
        
elif fruit == "Mango":
    
    if size == "small":
        price = 36.66 * 2
        
    elif size == "big":
        price = 19.60 * 5
        
elif fruit == "Pineapple":
    
    if size == "small":
        price = 42.10 * 2
        
    elif size == "big":
        price = 24.80 * 5
        
elif fruit == "Raspberry":
    
    if size == "small":
        price = 20 * 2
        
    elif size == "big":
        price = 15.20 * 5

order_price = price * ordered

if 400 <= order_price <= 1000:
    order_price *= 0.85
    
elif order_price > 1000:
    order_price *= 0.5

print(f"{order_price:.2f} lv.")
