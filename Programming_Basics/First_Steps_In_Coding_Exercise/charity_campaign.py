campaign_days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

baker_cakes = cakes * 45
baker_waffles = waffles * 5.80
baker_pancakes = pancakes * 3.20

all_bakers_daily = (baker_cakes + baker_waffles + baker_pancakes) * bakers
before_expenses = all_bakers_daily * campaign_days
after_expenses = (before_expenses / 8) * 7

print(after_expenses)
