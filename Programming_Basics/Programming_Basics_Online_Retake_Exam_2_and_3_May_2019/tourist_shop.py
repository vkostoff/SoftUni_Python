budget = float(input())
command = input()

money = budget
counter = 0
product_price = 0
money_over = False

while command != "Stop":
    product_name = command
    product_price = float(input())
    counter += 1
    
    if counter % 3 == 0:
        product_price *= 0.5
    if product_price > budget:
        money_over = True
        break
    else:
        budget -= product_price
    command = input()
    
if money_over:
    print(f"You don't have enough money!")
    print(f"You need {product_price - budget:.2f} leva!")
else:
    print(f"You bought {counter} products for {abs(budget - money):.2f} leva.")
