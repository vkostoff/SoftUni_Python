strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

strawberries_sum = strawberries_quantity * strawberries_price
raspberries_sum = raspberries_quantity * raspberries_price
oranges_sum = oranges_quantity * oranges_price
bananas_sum = bananas_quantity * bananas_price

print(strawberries_sum + raspberries_sum + oranges_sum + bananas_sum)
