'''
W A P goes through users input and stop as soon as it find the first even number .
'''
while True:
    num = int(input("Enter a number"))
    if num % 2 == 0:
        print("First Even number found :", num)
        break

