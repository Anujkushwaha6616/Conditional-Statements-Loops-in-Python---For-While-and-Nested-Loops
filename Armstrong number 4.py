#Check the given number is armstrong or not 
n = int(input("enter number to check armstrong or not:"))
num = n
result = 0 
powers = len(str(n))

while num>0 :
      ld = num%10
      result = result + ld**powers
      num = num//10 
print (result == n)    
