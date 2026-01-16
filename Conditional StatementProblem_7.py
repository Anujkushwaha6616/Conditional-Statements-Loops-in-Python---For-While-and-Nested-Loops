'''
Given an array, count how many elements are strictly greater than every element before them.
Input: [3, 4, 2, 7, 5, 9]
Output: 4
'''
def count_greater_previous(arr):
    count = 0
    current_max = float('-inf')

    for num in arr:
        if num > current_max:
            count += 1
            current_max = num

    return count

print(count_greater_previous([3, 4, 2, 7, 5, 9]))

