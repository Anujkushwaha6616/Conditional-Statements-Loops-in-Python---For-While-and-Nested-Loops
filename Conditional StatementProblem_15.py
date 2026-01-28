'''
Problem

Given a number, perform steps:

If number is even → divide by 2

If number is odd → subtract 1
Count how many steps are required to reach 1.

Example
Input:  n = 14
Output: 5
Explanation:
14→7→6→3→2→1 → total 5 steps
'''
def steps_to_one(n):
    steps = 0

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1

    return steps


print(steps_to_one(14))

