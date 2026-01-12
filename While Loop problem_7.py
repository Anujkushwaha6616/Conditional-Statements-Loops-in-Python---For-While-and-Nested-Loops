'''
Implement a coundown that start from a users given number and decresing to 1 , display the remaining time at each step

'''
second = int(input("Enter a number totart coundown :"))

while second > 0:
    print("time left:", second )
    second -= 1
if second == 0 :
    
    print("Let's Go ")
    
