rent = int(input())

statues_price = rent * 0.7
catering = statues_price * 0.85
sound = catering / 2
expenses = rent + statues_price + catering + sound

print(f"{expenses:.2f}")
