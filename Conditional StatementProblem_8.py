'''
Given an array, print how many times each number appears.
Input: [1, 2, 2, 3, 1, 4]
Output: {1: 2, 2: 2, 3: 1, 4: 1}
'''
def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(frequency([1, 2, 2, 3, 1, 4]))


