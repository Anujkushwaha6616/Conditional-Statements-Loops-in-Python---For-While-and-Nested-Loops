'''
Given three numbers a, b, and c. You need to find which is the greatest of them all.

Examples:

Input: a = 1, b = 2, c = 3
Output: 3
Explanation: Clearly, c = 3 is the greatest of (1, 2, 3)
'''# Input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Find greatest
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

# Output
print("Greatest number is:", greatest)
