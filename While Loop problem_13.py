'''
Problem: Reverse the Digits of a Number Using While Loop
Example

Input: 12345
Output: 54321
'''
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

print(reverse_number(12345))
