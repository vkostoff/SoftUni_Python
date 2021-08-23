stadium_capacity = int(input())
all_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for capacity in range(1, all_fans + 1):
    fan_in_sector = input()
    if fan_in_sector == "A":
        sector_a += 1
    if fan_in_sector == "B":
        sector_b += 1
    if fan_in_sector == "V":
        sector_v += 1
    if fan_in_sector == "G":
        sector_g += 1

sector_a_percentage = sector_a / all_fans * 100
sector_b_percentage = sector_b / all_fans * 100
sector_v_percentage = sector_v / all_fans * 100
sector_g_percentage = sector_g / all_fans * 100
total_fans_percentage = all_fans / stadium_capacity * 100

print(f"{sector_a_percentage:.2f}%")
print(f"{sector_b_percentage:.2f}%")
print(f"{sector_v_percentage:.2f}%")
print(f"{sector_g_percentage:.2f}%")
print(f"{total_fans_percentage:.2f}%")
