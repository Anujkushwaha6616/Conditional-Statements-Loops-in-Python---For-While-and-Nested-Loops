#Extraction of digits which is provided by user.
n = int(input("enter number : "))
num = n
#While loop
while num > 0:
    last_digit = num%10
    num = num//10
    print(last_digit)
