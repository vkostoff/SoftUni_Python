number = int(input())

increasing = 0
decreasing = 0

for number in range(1, number + 1):
    increasing += 1
    print(increasing * "*")
    
for number in range((increasing - 1), 0, -1):
    increasing -= 1
    print(increasing * "*")
