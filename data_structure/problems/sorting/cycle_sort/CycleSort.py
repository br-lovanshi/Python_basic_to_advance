# if the range is 1 to n
def sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]-1
        if nums[i] != nums[correct]:
            # swap
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1

# if the range is 0 to n
def sort_from_zero(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[correct]:
            # swap
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1
        # in the array.
        # The algorithm works by iterating through the array and placing
        # each element in its correct position.
        # The algorithm is not stable, meaning that the relative order of
        # equal elements may not be preserved.


# Example usage
nums = [3, 5, 2, 1, 4]
print(nums)
sort(nums)
print(nums)
nums1 = [2,0,5,3,1,4]
sort_from_zero(nums1)
print(nums1)

# Output: [1, 2, 3, 4, 5]
# Time complexity: O(n)
# Space complexity: O(1)
# This implementation assumes that the numbers are in the range 1 to n
# and that there are no duplicates.
# If the numbers are not in the range 1 to n, we need to modify the code
# to handle that case.
# The code above is a simple implementation of Cycle Sort.
# Cycle Sort is an in-place, non-comparison based sorting algorithm
# that is based on the idea of placing each element in its correct position