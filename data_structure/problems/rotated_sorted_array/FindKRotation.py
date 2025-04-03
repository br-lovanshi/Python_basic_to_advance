def findKRotation(arr : [int]) -> int:
    # Write your code here.
    index = pivot(arr)
    return index

def pivot(arr):
    start = 0
    end = len(arr)-1
    if arr[start] < arr[end]:
        return 0

    while start < end:
        mid = start + (end - start)//2
        if arr[mid] < arr[mid -1]:
            return mid
        elif arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1
    return start

# arr = [1, 2, 3, 4, 5]
# print(findKRotation(arr)) # Output: 0
# arr = [4, 5, 6, 7, 0, 1, 2]
# print(findKRotation(arr)) # Output: 4
# arr = [3, 4, 5, 1, 2]
# print(findKRotation(arr)) # Output: 3
# write this test case 
arr = [35, 43, 45, 1, 2, 9, 12, 13, 19, 20, 26, 28, 29, 32 ]
print(findKRotation(arr)) # Output: 3
# This function finds the number of times a sorted array has been rotated.

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Problem Link:
#https://www.naukri.com/code360/problems/rotation_7449070?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
# https://takeuforward.org/arrays/find-out-how-many-times-the-array-has-been-rotated/