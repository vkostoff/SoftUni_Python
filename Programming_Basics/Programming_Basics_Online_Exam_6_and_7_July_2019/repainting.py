nylon_needed = int(input())
needed_paint = int(input())
diluent_needed = int(input())
working_hours = int(input())

nylon_price = (nylon_needed + 2) * 1.5
paint_price = (needed_paint * 1.1) * 14.5
diluent_price = diluent_needed * 5
materials_price = nylon_price + paint_price + diluent_price + 0.4
work_price = (materials_price * 0.3) * working_hours
all_expenses = materials_price + work_price

print(f"Total expenses: {all_expenses:.2f} lv.")