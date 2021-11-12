numbers = [int(x) for x in input().split(", ")]
positive = [str(x) for x in numbers if x >= 0]
positive = ", ".join(positive)
negative = [str(x) for x in numbers if x < 0]
negative = ", ".join(negative)
even = [str(x) for x in numbers if x % 2 == 0]
even = ", ".join(even)
odd = [str(x) for x in numbers if not x % 2 == 0]
odd = ", ".join(odd)
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
