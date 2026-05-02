#Extraction of digits using loops
n = int(input("enter number : "))
num = n
#loop
while num > 0:
    last_digit = num%10
    print(last_digit)
    num = num//10
