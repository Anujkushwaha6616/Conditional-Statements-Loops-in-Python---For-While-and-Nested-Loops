'''
Problem

Given a number, reverse its digits only until you encounter the first even digit.
Return the partially reversed number.

Example
Input:  n = 75319
Output: 913 
'''
def reverse_until_even(n):
    rev = 0

    while n > 0:
        digit = n % 10
        
        # Remove the digit from n in every iteration
        n //= 10

        # Check if digit is even → stop immediately
        if digit % 2 == 0:
            break
        
        # Otherwise add to reverse
        rev = rev * 10 + digit

    return rev


print(reverse_until_even(75319))

