prime = 0
non_prime = 0

is_prime = True

command = input()

while command != "stop":
    number = int(command)
    
    if number < 0:
        print("Number is negative.")
        
    elif number == 1:
        non_prime += 1
        
    elif number > 1:
        
        for n in range(2, number):
            
            if (number % n) == 0 and n != number:
                is_prime = False
                break
                
            else:
                is_prime = True
                
        if is_prime:
            prime += number
            
        else:
            non_prime += number
            
    command = input()

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
