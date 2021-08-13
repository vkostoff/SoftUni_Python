mackerel_price = float(input())
sprat_price = float(input())
bonito_kgs = float(input())
scad_kgs = float(input())
mussels_kgs = int(input())

bonito_price = mackerel_price * 1.6
scad_price = sprat_price * 1.8
mussels_price = 7.5

mussels_total = mussels_kgs * mussels_price
scad_total = scad_kgs * scad_price
bonito_total = bonito_kgs * bonito_price

print("%.2f" % (mussels_total + scad_total + bonito_total))
