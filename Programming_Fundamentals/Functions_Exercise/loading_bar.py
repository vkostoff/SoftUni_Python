def loading_bar(a):
    b = ""
    if a < 100:
        for i in range(0, (a // 10)):
            b += "%"
        for j in range(0, (10 - (a // 10))):
            b += "."
        print(f"{a}% [{b}]")
        print("Still loading...")
    elif a == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


number = int(input())
loading_bar(number)
