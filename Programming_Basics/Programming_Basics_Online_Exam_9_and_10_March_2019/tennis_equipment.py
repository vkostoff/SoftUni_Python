from math import floor, ceil
tennis_rocket_price = float(input())
tennis_rockets_count = int(input())
sneakers_count = int(input())
tennis_rockets_total = tennis_rockets_count * tennis_rocket_price
sneakers_price = tennis_rocket_price / 6
sneakers_total = sneakers_price * sneakers_count
others_price = (tennis_rockets_total + sneakers_total) * 0.2
total_price = tennis_rockets_total + sneakers_total + others_price
paid_by_jokovic = total_price / 8
paid_by_sponsors = total_price / 8 * 7
print(f"Price to be paid by Djokovic {floor(paid_by_jokovic)}")
print(f"Price to be paid by sponsors {ceil(paid_by_sponsors)}")
