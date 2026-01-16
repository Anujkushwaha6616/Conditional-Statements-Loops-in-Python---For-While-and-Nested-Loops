'''
Problem: Find Elements Appearing More Than Once
Example

Input: [4, 5, 1, 2, 5, 3, 1]
Output: [5, 1]
'''
def find_duplicates(arr):
    seen = set()
    dup = []

    for num in arr:
        if num in seen:
            dup.append(num)
        else:
            seen.add(num)

    return dup

print(find_duplicates([4, 5, 1, 2, 5, 3, 1]))
