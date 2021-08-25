name_aviocompany = input()
adult_tickets_count = int(input())
kids_tickets_count = int(input())
net_price_adult_tickets = float(input())
net_service_fee = float(input())
net_price_kids_tickets = net_price_adult_tickets * 0.30
total_price_kids_tickets = net_price_kids_tickets + net_service_fee
total_price_adult_tickets = net_price_adult_tickets + net_service_fee
profit = ((adult_tickets_count * total_price_adult_tickets) + (kids_tickets_count * total_price_kids_tickets)) * 0.2

print(f"The profit of your agency from {name_aviocompany} tickets is {profit:.2f} lv.")
