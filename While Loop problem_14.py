'''
Problem: Find the Sum of Digits Until the Number Becomes Single Digit
Input: 987
Output: 6
'''
def digit_sum_until_one(n):
    while n > 9:
        temp = 0
        while n > 0:
            temp += n % 10
            n //= 10
        n = temp
    return n

print(digit_sum_until_one(987))

