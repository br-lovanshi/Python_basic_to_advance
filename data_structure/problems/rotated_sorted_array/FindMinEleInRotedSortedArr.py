def find_min(arr):
    start = 0
    end = len(arr) - 1

    if arr[start] < arr[end]:
        return arr[start]
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start]

# This function finds the minimum element in a rotated sorted array.
# It uses binary search to efficiently locate the minimum element.
# The function first checks if the array is already sorted (not rotated).
# If it is sorted, it returns the first element.
# If the array is rotated, it uses binary search to find the pivot point
# where the rotation occurs, and returns the minimum element.
# The function has a time complexity of O(log n) and a space complexity of O(1).
# The function takes an array as input and returns the minimum element.
# test cases
print(find_min([4, 5, 6, 7, 0, 1, 2])) # Output: 0
print(find_min([1, 2, 3, 4, 5])) # Output: 1
print(find_min([3, 4, 5, 1, 2])) # Output: 1
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Problem Link:
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/