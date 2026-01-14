'''

'''
number = int(input("Enter value:"))
i = 1
squre = False

while i * i <= number:
    if i * i == number:
        squre = True
        break
    i += 1
if squre:
    print(f"{number} is perfect squre")
else:
    print(f"{number} is not a perfect squre")
    
