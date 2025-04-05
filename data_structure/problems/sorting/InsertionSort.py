def sort(nums):
    n = len(nums)
    for i in range(n-1):
        j = i + 1
        while j > 0 and nums[j] < nums[j-1]:
            swap(nums, j, j-1)
            j -= 1

# Function to swap two elements in the list
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp



# test case
nums = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", nums)
sort(nums)
print("Sorted array:", nums)
# Time Complexity: O(n^2)           