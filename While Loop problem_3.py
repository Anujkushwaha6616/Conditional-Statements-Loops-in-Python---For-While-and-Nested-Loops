'''
W A P to print all odd number frm 1 to 10
Expected Output: 1,3,5,7,9
'''
number = 1
while number <= 10:
    if number % 2 != 0:
        print(number, end=" ")
    number +=1
