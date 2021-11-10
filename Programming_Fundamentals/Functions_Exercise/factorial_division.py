def factoral_division(a, b):
    first_factoral = a
    second_factoral = b
    
    for i in range(a-1, 0, -1):
        first_factoral *= i
        
    for j in range(b-1, 0, -1):
        second_factoral *= j
        
    result = first_factoral / second_factoral
    
    return result


first_number = int(input())
second_number = int(input())

print(f"{factoral_division(first_number, second_number):.2f}")
