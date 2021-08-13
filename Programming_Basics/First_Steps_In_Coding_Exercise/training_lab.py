w = float(input())
h = float(input())

w_cm = int(w * 100 / 120)
h_cm = int(((h * 100) - 100) / 70)
result = w_cm * h_cm

print(result - 3)
