'''
W A P goes through users input and stop as soon as it find the first even number .
Expected output:first even number found:2
'''
while True:
    num = int(input("Enter a number"))
    if num % 2 == 0:
        print("First Even number found :", num)
        break


