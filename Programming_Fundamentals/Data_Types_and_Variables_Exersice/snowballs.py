import sys

snowballs = int(input())

snowball_value = -sys.maxsize
snowball_snow_a = 0
snowball_time_a = 0
snowball_quality_a = 0

for i in range(1, snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    
    if current_snowball_value > snowball_value:
        snowball_value = current_snowball_value
        snowball_snow_a = snowball_snow
        snowball_time_a = snowball_time
        snowball_quality_a = snowball_quality
        
print(f"{snowball_snow_a} : {snowball_time_a} = {snowball_value} ({snowball_quality_a})")
