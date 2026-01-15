'''
The continue statement in Python returns the control to the beginning of the loop.
'''
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
