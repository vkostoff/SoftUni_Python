drink = input()
quantity = int(input())


def total_price(a, b):
    price = None
    if a == "coffee":
        price = 1.5
    elif a == "water":
        price = 1
    elif a == "coke":
        price = 1.4
    elif a == "snacks":
        price = 2
    return price * b


print(f"{total_price(drink, quantity):.2f}")
