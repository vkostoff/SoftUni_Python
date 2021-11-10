numbers = input().split(", ")


def palindrome(a):
    is_palindrome = []
    
    for i in a:
        if i == i[::-1]:
            is_palindrome.append(True)
            
        else:
            is_palindrome.append(False)
            
    for j in is_palindrome:
        print(j)


palindrome(numbers)
