vegetables_price = float(input())
fruits_price = float(input())
kgs_vegetables = float(input())
kgs_fruits = float(input())

total_vegetables = vegetables_price * kgs_vegetables
total_fruits = fruits_price * kgs_fruits
total_sum = (total_fruits + total_vegetables) / 1.94

print("%.2f" % total_sum)
