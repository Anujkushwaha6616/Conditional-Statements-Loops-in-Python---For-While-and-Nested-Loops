'''
Problem

Given an array of integers and a number K, count how many subarrays have a sum exactly equal to K.

You must consider every possible subarray, which leads to a nested loop approach.

Example

Input:
arr = [3, 4, 7, 2, -3, 1, 4, 2], K = 7
Output:
4

'''def count_subarrays_sum_k(arr, k):
    count = 0

    for start in range(len(arr)):
        current_sum = 0

        for end in range(start, len(arr)):
            current_sum += arr[end]

            if current_sum == k:
                count += 1

    return count

# Example
arr = [3, 4, 7, 2, -3, 1, 4, 2]
K = 7
print(count_subarrays_sum_k(arr, K))

