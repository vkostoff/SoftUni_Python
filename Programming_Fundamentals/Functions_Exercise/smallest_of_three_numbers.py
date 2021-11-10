number_one = int(input())
number_two = int(input())
number_three = int(input())


def smallest_integer(a, b, c):
    smallest = 0
    
    if a < b and a < c:
        smallest = a
        
    elif b < a and b < c:
        smallest = b
        
    elif c < a and c < b:
        smallest = c
        
    return smallest


print(smallest_integer(number_one, number_two, number_three))
