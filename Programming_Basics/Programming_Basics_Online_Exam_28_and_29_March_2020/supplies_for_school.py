pen_count = int(input())
marker_count = int(input())
cleaner = float(input())
discount = int(input())

pen_price = pen_count * 5.80
marker_price = marker_count * 7.2
cleaner_price = cleaner * 1.2
total_discount = (pen_price + marker_price + cleaner_price) * (discount / 100)
total_price = (pen_price + marker_price + cleaner_price) - total_discount

print(f"{total_price:.3f}")
