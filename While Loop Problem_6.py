'''
W A P to count the number of consonant in the word "Learning"
Expected Output: 5
'''
word = input("Enter a word to check number of consonant:")
index = 0
count = 0
vowels = "a e i o u"

while index < len(word):
    if word[index].lower() not in vowels and word[index] :
        count += 1
    index += 1

print(count)        
