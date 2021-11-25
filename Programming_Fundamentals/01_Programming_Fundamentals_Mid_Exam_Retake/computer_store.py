total_price = 0
special = False
token = input()
while True:
    if token == "special":
        special = True
        break
    elif token == "regular":
        break
    else:
        price = float(token)
        if price < 0:
            print("Invalid price!")
        else:
            total_price += price
    token = input()
taxes = total_price * 0.2
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if not special:
        print(f"Total price: {(total_price + taxes):.2f}$")
    else:
        print(f"Total price: {((total_price + taxes) * 0.9):.2f}$")
