total_sum = int(input())

counter = 0
cash_count = 0
card_count = 0
cash_money = 0
card_money = 0
total_money = 0

command = input()

while command != "End":
    item_price = int(command)
    counter += 1
    
    if counter % 2 == 0:
        
        if item_price < 10:
            print("Error in transaction!")
            
        else:
            card_count += 1
            card_money += item_price
            total_money += item_price
            print("Product sold!")
            
    else:
        
        if item_price > 100:
            print("Error in transaction!")
            
        else:
            cash_count += 1
            cash_money += item_price
            total_money += item_price
            print("Product sold!")
            
    if total_sum <= total_money:
        print(f"Average CS: {cash_money / cash_count:.2f}")
        print(f"Average CC: {card_money / card_count:.2f}")
        break
        
    command = input()
    
else:
    print("Failed to collect required money for charity.")
