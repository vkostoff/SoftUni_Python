budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
liter_milk_price = flour_price * 1.25
milk_price = liter_milk_price / 4
price_per_cozonac = flour_price + eggs_price + milk_price
colored_eggs = 0
cozonacs = 0

while budget > price_per_cozonac:
    colored_eggs += 3
    cozonacs += 1
    budget -= price_per_cozonac
    
    if cozonacs % 3 == 0:
        colored_eggs -= (cozonacs - 2)
        
print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
