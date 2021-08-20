chrysanthemum_bought = int(input())
roses_bought = int(input())
tulips_bought = int(input())
season = input()
holiday = input()

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bouquet_price = (chrysanthemum_price * chrysanthemum_bought) + (tulips_bought * tulips_price) \
    + (roses_bought * roses_price)

total_flowers = chrysanthemum_bought + tulips_bought + roses_bought

if holiday == "Y":
    bouquet_price *= 1.15

if tulips_bought > 7 and season == "Spring":
    bouquet_price *= 0.95
elif roses_bought >= 10 and season == "Winter":
    bouquet_price *= 0.90
if total_flowers > 20:
    bouquet_price *= 0.80

total_price = bouquet_price + 2

print(f"{total_price:.2f}")
