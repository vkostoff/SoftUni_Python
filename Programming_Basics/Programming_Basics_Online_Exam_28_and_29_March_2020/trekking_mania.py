groups_count = int(input())

all_people = 0
musala = 0
montblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for groups in range(1, groups_count + 1):
    people_count = int(input())
    all_people += people_count
    
    if people_count <= 5:
        musala += people_count
        
    elif 6 <= people_count <= 12:
        montblan += people_count
        
    elif 13 <= people_count <= 25:
        kilimanjaro += people_count
        
    elif 26 <= people_count <= 40:
        k2 += people_count
        
    elif people_count >= 41:
        everest += people_count

print(f"{musala / all_people * 100:.2f}%")
print(f"{montblan / all_people * 100:.2f}%")
print(f"{kilimanjaro / all_people * 100:.2f}%")
print(f"{k2 / all_people * 100:.2f}%")
print(f"{everest / all_people * 100:.2f}%")
