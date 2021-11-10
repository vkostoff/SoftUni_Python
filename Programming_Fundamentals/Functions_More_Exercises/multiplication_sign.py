def multiplication_sign(a, b, c):
    if a < 0:
        if b < 0 < c:
            return "positive"
        elif b > 0 > c:
            return "positive"
        elif b > 0 and c > 0:
            return "negative"
        elif b < 0 and c < 0:
            return "negative"
        elif b == 0 or c == 0:
            return "zero"
    elif a > 0:
        if b < 0 and c < 0:
            return "positive"
        elif b > 0 > c:
            return "negative"
        elif b > 0 and c > 0:
            return "positive"
        elif b == 0 or c == 0:
            return "zero"
    elif a == 0:
        return "zero"
    elif b < 0:
        if a < 0 < c:
            return "positive"
        elif a > 0 > c:
            return "positive"
        elif a > 0 and c > 0:
            return "negative"
        elif a < 0 and c < 0:
            return "negative"
        elif a == 0 or c == 0:
            return "zero"
    elif b > 0:
        if a < 0 and c < 0:
            return "positive"
        elif a > 0 > c:
            return "negative"
        elif a > 0 and c > 0:
            return "positive"
        elif a == 0 or c == 0:
            return "zero"
    elif b == 0:
        return "zero"
    elif c < 0:
        if a < 0 < b:
            return "positive"
        elif a > 0 > b:
            return "positive"
        elif a > 0 and b > 0:
            return "negative"
        elif b < 0 and a < 0:
            return "negative"
        elif a == 0 or b == 0:
            return "zero"
    elif c > 0:
        if a < 0 and b < 0:
            return "positive"
        elif a > 0 > b:
            return "negative"
        elif a > 0 and b > 0:
            return "positive"
        elif a == 0 or b == 0:
            return "zero"
    elif c == 0:
        return "zero"


first = int(input())
second = int(input())
third = int(input())
print(multiplication_sign(first, second, third))
