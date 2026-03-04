"""
Output:
0 1 2 3 4 
0 1 2 3 
0 1 2
0 1
0
"""
n=5

for i in range (n, 0, -1):
    for j in range(i):
        print("j" , end=" ")

    print()    

