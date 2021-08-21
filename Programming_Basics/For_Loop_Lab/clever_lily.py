age = int(input())
price_laundry = float(input())
toy_price = int(input())

total_toys = 0
saved_money = 0

for birthday in range(1, age + 1):
    
    if birthday % 2 == 1:
        total_toys += 1
        
    else:
        saved_money += birthday * 5 - 1

total_money = saved_money + (total_toys * toy_price)

if total_money >= price_laundry:
    money_left = total_money - price_laundry
    print(f"Yes! {money_left:.2f}")
    
else:
    money_needed = price_laundry - total_money
    print(f"No! {money_needed:.2f}")
