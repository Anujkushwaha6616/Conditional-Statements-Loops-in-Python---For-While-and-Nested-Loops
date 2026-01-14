'''
W A P to check if the given number such as 16 is a perfect squre or not 
Expected output: 16 is a perfecr squre
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
    

