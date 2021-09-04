one_lev = int(input())
two_leva = int(input())
five_leva = int(input())
total_sum = int(input())
money = total_sum
for a in range(0, one_lev + 1):
    for b in range(0, two_leva + 1):
        for c in range(0, five_leva + 1):
            if (a * 1) + (b * 2) + (c * 5) == total_sum:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total_sum} lv.")
