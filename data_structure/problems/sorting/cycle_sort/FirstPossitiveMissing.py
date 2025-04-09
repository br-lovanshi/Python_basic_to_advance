def sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]-1
        if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[correct]:
            # swap
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1

def find_missing(nums):
    sort(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

# Example usage
nums = [3,4,-1,1]
print("Missing number:", find_missing(nums))

# Output: 2
nums1 = [1]
print(find_missing(nums1))


# Time complexity: O(n)
# Space complexity: O(1)
# https://leetcode.com/problems/first-missing-positive/