'''
Given an array of integers and a number K, count how many unique quadruplets (i, j, m, n) exist such that:

arr[i] + arr[j] + arr[m] + arr[n] = K


Use 4 nested loops (pure brute force, advanced-level).

Example

Input:
arr = [1, 0, -1, 0, -2, 2], K = 0

Output:
3
'''
def count_quadruplets(arr, K):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                for n2 in range(m + 1, n):
                    if arr[i] + arr[j] + arr[m] + arr[n2] == K:
                        count += 1

    return count

# Example
arr = [1, 0, -1, 0, -2, 2]
K = 0
print(count_quadruplets(arr, K))  # Output: 3

