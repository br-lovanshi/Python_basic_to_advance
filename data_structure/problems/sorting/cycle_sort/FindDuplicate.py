def sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]-1
        if nums[i] != nums[correct]:
            # swap
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1

def find_duplicate(nums):
    sort(nums)
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]
    return -1
    
# Example usage
nums = [3, 4, 1, 1]
print("Duplicate number:", find_duplicate(nums))
# Output: 2
nums1 = []
print("Duplicate number:", find_duplicate(nums1))

# Problem: Find the duplicate number in an array of n integers
# https://leetcode.com/problems/find-the-duplicate-number/description/