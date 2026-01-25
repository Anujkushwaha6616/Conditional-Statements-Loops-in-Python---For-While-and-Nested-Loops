'''
Problem:

Given a number, keep removing digits from the end (right side) using a loop until the sum of removed digits becomes greater than 20.
Return how many digits were removed.

Example
Input:  n = 987654
Output: 3
'''
def count_removed_digits(n):
    removed = 0
    total = 0

    while n > 0 and total <= 20:
        digit = n % 10
        total += digit
        removed += 1
        n //= 10

    return removed


print(count_removed_digits(987654))

