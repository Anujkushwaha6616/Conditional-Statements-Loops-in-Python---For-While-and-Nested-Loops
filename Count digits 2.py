#count the digit of the given number .

n = input("Enter to count value of digit:")
count = 0
num =int(n)
while num > 0:
    num = num//10
    count+=1
print(count) 
