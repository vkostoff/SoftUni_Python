items_list = list(input().split(sep="|"))
budget = float(input())
temporary_list = []
old_price = 0
expenses = 0
bought = []
for item in items_list:
    if "Clothes" in item:
        temporary_list = item.split(sep="->")
        if float(temporary_list[1]) > 50:
            continue
        elif float(temporary_list[1]) <= budget:
            old_price += float(temporary_list[1])
            budget -= float(temporary_list[1])
            bought.append(float(temporary_list[1]) * 1.4)
    elif "Shoes" in item:
        temporary_list = item.split(sep="->")
        if float(temporary_list[1]) > 35:
            continue
        elif float(temporary_list[1]) <= budget:
            old_price += float(temporary_list[1])
            budget -= float(temporary_list[1])
            bought.append(float(temporary_list[1]) * 1.4)
    elif "Accessories" in item:
        temporary_list = item.split(sep="->")
        if float(temporary_list[1]) > 20.5:
            continue
        elif float(temporary_list[1]) <= budget:
            old_price += float(temporary_list[1])
            budget -= float(temporary_list[1])
            bought.append(float(temporary_list[1]) * 1.4)
new_number = 0
for i in bought:
    new_number += i
    print(f"{i:.2f}", end=" ")
print()
print(f"Profit: {abs(old_price - new_number):.2f}")
new_budget = budget + new_number
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
