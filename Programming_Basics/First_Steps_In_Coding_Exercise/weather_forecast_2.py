degrees = float(input())

if degrees >= 35.1:
    print("unknown")

elif degrees >= 26 <= 35:
    print("Hot")

elif degrees >= 20.1 <= 25.9:
    print("Warm")

elif degrees >= 15 <= 20:
    print("Mild")

elif degrees >= 12 <= 14.9:
    print("Cool")

elif degrees >= 5 <= 11.9:
    print("Cold")

else:
    print("unknown")
