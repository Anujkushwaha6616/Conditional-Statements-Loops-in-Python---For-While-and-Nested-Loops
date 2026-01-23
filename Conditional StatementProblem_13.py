'''
Problem (Advanced Nested Loop)

Count the number of "special pairs" (i, j) in an array such that:

i < j

arr[j] - arr[i] = j - i

Dono condition sahi hon tabhi pair special maana jaayega.

Example

Input:
arr = [3, 4, 6, 7, 9]

Check pairs manually:

Pair (0,1): 4 - 3 = 1 AND 1 - 0 = 1 → ✔ special

Pair (1,2): 6 - 4 = 2 AND 2 - 1 = 1 → ❌

Pair (2,3): 7 - 6 = 1 AND 3 - 2 = 1 → ✔ special

Pair (3,4): 9 - 7 = 2 AND 4 - 3 = 1 → ❌

Output:
2
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

