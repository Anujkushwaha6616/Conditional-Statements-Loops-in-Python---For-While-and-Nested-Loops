n = int(input("Enter number:"))
num = n
result = 0

while num>0:
    ld = num%10
    result =(result*10)+ld
    num = num//10


print( n == result)