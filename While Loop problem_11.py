'''
W A P to count the occurence of the latter in the given word
'''
string = input("Enter a string:")
char_to_count = input("enter charecter to count occurence:")
count = 0
index = 0

while index < len(string):
    if string[index] == char_to_count:
        count += 1
    index +=1
print(f"{char_to_count} = {count}")    
