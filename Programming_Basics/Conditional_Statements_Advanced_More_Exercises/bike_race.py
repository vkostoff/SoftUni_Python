from math import ceil

juniors = int(input())
seniors = int(input())
trace_type = input()
juniors_tax = 0
seniors_tax = 0

if trace_type == "trail":
    juniors_tax = 5.50
    seniors_tax = 7
elif trace_type == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.50
    if (juniors + seniors) >= 50:
        juniors_tax *= 0.75
        seniors_tax *= 0.75
elif trace_type == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75
elif trace_type == "road":
    juniors_tax = 20
    seniors_tax = 21.50

total_tax = ((juniors_tax * juniors) + (seniors_tax * seniors)) * 0.95

print(f"{total_tax:.2f}")
