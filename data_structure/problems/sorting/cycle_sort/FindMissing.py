def sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[correct]:
            # swap
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1

def find_missing(nums):
    sort(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)


nums1 = [2, 0, 5, 3, 1, 4]
sort(nums1)
print(nums1)
missing = find_missing(nums1)
print("Missing number:", missing)
# Output: [1, 2, 3, 4, 5]
# Time complexity: O(n)
# Space complexity: O(1)
# This implementation assumes that the numbers are in the range 0 to n
# Problem: Find the missing number in an array of n integers
# https://leetcode.com/problems/missing-number/