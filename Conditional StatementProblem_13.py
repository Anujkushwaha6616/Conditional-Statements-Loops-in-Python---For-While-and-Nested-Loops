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
