chicken_count = int(input())
fish_count = int(input())
vegetarian_count = int(input())
chicken_price = chicken_count * 10.35
fish_price = fish_count * 12.4
vegetarian_price = vegetarian_count * 8.15
total = vegetarian_price + chicken_price + fish_price
dessert_price = total * 0.2
total_price = total + dessert_price + 2.5
print(f"Total: {total_price:.2f}")