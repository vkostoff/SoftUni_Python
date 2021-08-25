joinery_count = int(input())
joinery_type = input()
delivery = input()

if joinery_count < 10:
    print("Invalid order")
    exit()

if joinery_type == "90X130":
    if joinery_count <= 30:
        price = joinery_count * 110
    elif 30 < joinery_count <= 60:
        price = (joinery_count * 110) * 0.95
    else:
        price = (joinery_count * 110) * 0.92

elif joinery_type == "100X150":
    if joinery_count <= 40:
        price = joinery_count * 140
    elif 40 < joinery_count <= 80:
        price = (joinery_count * 140) * 0.94
    else:
        price = (joinery_count * 140) * 0.90

elif joinery_type == "130X180":
    if joinery_count <= 20:
        price = joinery_count * 190
    elif 20 < joinery_count <= 50:
        price = (joinery_count * 190) * 0.93
    else:
        price = (joinery_count * 190) * 0.88

elif joinery_type == "200X300":
    if joinery_count <= 25:
        price = joinery_count * 250
    elif 25 < joinery_count <= 50:
        price = (joinery_count * 250) * 0.91
    else:
        price = (joinery_count * 250) * 0.86

if delivery == "With delivery":
    price += 60
elif delivery == "Without delivery":
    pass

if joinery_count > 99:
    price *= 0.96

print(f"{price:.2f} BGN")
