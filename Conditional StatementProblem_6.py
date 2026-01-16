'''
a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 
Input: n = 5
Output: 5 10 15 20 25 30 35 40 45 50
'''
n = int(input("Enter an intrger:"))

# Your code here
for i in range (1,11):
    print(n*i, end=" ")

