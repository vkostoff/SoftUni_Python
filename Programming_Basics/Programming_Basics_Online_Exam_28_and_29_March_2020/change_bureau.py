bitcoin = int(input())
chinese = float(input())
commission = float(input())

bitcoin_price = bitcoin * 1168
chinese_price_dollar = chinese * 0.15
dollar = 1.76
euro = 1.95

leva = (bitcoin_price + (chinese_price_dollar * dollar))
euro_money = leva / euro
commission_percentage = (commission / 100) * euro_money
total_money = euro_money - commission_percentage

print(f"{total_money:.2f}")
