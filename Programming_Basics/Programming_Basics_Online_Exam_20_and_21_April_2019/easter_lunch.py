breads_count = int(input())
egg_cartons = int(input())
cookies_kg = int(input())

breads_price = breads_count * 3.2
egg_price = egg_cartons * 4.35
cookies_price = cookies_kg * 5.4
paint_price = (egg_cartons * 12) * 0.15
total = breads_price + egg_price + cookies_price + paint_price

print(f"{total:.2f}")
