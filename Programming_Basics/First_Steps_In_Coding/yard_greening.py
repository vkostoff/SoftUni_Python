square_meters = float(input())
end_price = square_meters * 7.61
discount = 0.18 * end_price

print(f"The final price is: {end_price - discount} lv.")
print(f"The discount is: {discount} lv.")