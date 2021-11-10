def password_checker(password):
    is_valid = True
    digits_counter = 0
    
    if len(password) == 0:
        print("Password must be between 6 and 10 characters")
        exit()
        
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
        
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
        
    for i in password:
        if i.isnumeric():
            digits_counter += 1
            
    if digits_counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")
        
    if is_valid:
        print("Password is valid")


string = input()

password_checker(string)
