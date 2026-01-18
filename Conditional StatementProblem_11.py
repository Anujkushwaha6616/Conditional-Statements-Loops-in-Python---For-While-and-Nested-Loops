'''
Problem

Given an array of integers and a number K, count how many unique triplets (i, j, k) exist such that:

arr[i] + arr[j] + arr[k] = K


This must be solved using three nested loops.

Example

Input:
arr = [2, 3, 1, 0, -1, 4], K = 5

Output:
3

'''
def count_triplets(arr, k):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                if arr[i] + arr[j] + arr[m] == k:
                    count += 1

    return count

# Example
arr = [2, 3, 1, 0, -1, 4]
K = 5
print(count_triplets(arr, K))
