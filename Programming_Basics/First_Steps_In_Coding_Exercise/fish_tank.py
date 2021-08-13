length = int(input())
width = int(input())
height = int(input())
used_volume_percentage = float(input())

total_volume = length * width * height
used_volume = (total_volume * used_volume_percentage) / 100

print((total_volume - used_volume) * 0.001)
