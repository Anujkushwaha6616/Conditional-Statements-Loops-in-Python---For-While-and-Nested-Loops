'''
Keep reading number from the user and calculate the sum until the input is 0.
'''
total = 0
number = int(input("Enter a number (Enter 0 for sum ):"))
while number != 0:
     total += number
     number = int(input("Enter a number(Enter 0 for sum ):"))
         
print("Total sum:",total)

