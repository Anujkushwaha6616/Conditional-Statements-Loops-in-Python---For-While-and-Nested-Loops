#find all factors of the given number
n = int(input("Enter to gert factor of given number:"))
num = n
result =[]

for i in range(1,num+1):
    if num%i == 0:
        result.append(i)
print(result)        
