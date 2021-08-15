number = float(input())
in_measure = input()
out_measure = input()

if in_measure == "mm" and out_measure == "m":
    result = number * 0.001
    print(f"{result:.3f}")

elif in_measure == "m" and out_measure == "mm":
    result = number * 1000
    print(f"{result:.3f}")

elif in_measure == "m" and out_measure == "cm":
    result = number * 100
    print(f"{result:.3f}")

elif in_measure == "cm" and out_measure == "m":
    result = number * 0.01
    print(f"{result:.3f}")

elif in_measure == "cm" and out_measure == "mm":
    result = number * 10
    print(f"{result:.3f}")

elif in_measure == "mm" and out_measure == "cm":
    result = number * 0.1
    print(f"{result:.3f}")