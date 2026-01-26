'''
Problem : Count the number of "special pairs" (i, j) in an array such that:
i < j
arr[j] - arr[i] = j - i
Dono condition sahi hon tabhi pair special maana jaayega.
Input: arr = [3, 4, 6, 7, 9]
Output: 2
'''
def count_special_pairs(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[j] - arr[i]) == (j - i):
                count += 1

    return count


# Example
arr = [3, 4, 6, 7, 9]
print(count_special_pairs(arr))  # Output: 2



