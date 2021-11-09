number = input()


def odd_and_even_sum(a):
    even_sum = 0
    odd_sum = 0
    
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
            
        elif not int(i) == 0:
            odd_sum += int(i)
            
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_and_even_sum(number))
