'''
W A P to reverse each word in the sentence "Hello World" using while loop
Expected Output: olleH dlroW
'''
sentence = input("Enter the input to print it's reverse:")
word = sentence.split()
for word in word:
    i = len(word) -1
    while i>=0:
        print(word[i], end=" ")
        i -= 1
    print(end=" ")    
