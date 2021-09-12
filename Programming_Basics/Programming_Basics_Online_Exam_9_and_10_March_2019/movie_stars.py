budget = float(input())

out_of_budget = False

command = input()

while command != "ACTION":
    actor_name = command
    
    if len(actor_name) > 15:
        budget *= 0.8
        
    else:
        commission = float(input())
        budget -= commission
        
    if budget <= 0:
        out_of_budget = True
        break
        
    command = input()
    
if out_of_budget:
    print(f"We need {abs(budget):.2f} leva for our actors.")
    
else:
    print(f"We are left with {budget:.2f} leva.")
