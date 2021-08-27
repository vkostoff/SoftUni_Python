total_money = 0
command = input()
while command != "NoMoreMoney":
    money_send = float(command)
    if money_send <= 0:
        print("Invalid operation!")
        break
    total_money += money_send
    print(f"Increase: {money_send:.2f}")
    command = input()
print(f"Total: {total_money:.2f}")
