deposit = float(input())
deposit_term = int(input())
yearly_interest = float(input())

monthly_interest = deposit * yearly_interest / 100 / 12

print(deposit + (deposit_term * monthly_interest))
