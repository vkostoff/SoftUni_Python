a1 = int(input())
a2 = int(input())
n = int(input())
c_end = n / 2
for a in range(a1, a2):
    for b in range(1, n):
        for c in range(1, int(c_end)):
            d = a
            if d % 2 != 0 and (b + c + d) % 2 != 0:
                print(f"{chr(a)}-{b}{c}{d}")