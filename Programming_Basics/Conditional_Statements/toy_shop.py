vacation_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = puzzles_count * 2.60
dolls_price = dolls_count * 3
bears_price = bears_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2

gross_profit = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
total_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

if total_count >= 50:
    gross_profit = gross_profit * 0.75

total_profit = gross_profit * 0.90
money_left = abs(vacation_price - total_profit)
money_needed = vacation_price - total_profit

if total_profit >= vacation_price:
    print(f"Yes! {money_left:.2f} lv left.")

else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")