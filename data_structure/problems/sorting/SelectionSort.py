# find the max element in the array and swap it with the last element
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Selection Sort

def sort(nums):
    for i in range(len(nums)):
        last_index = len(nums) - i - 1
        max_index = find_max(nums, 0, last_index)
        swap(nums, last_index, max_index)


def swap(nums, start, end):
    temp = nums[start]
    nums[start] = nums[end]
    nums[end] = temp


def find_max(nums, start, end):
    max_index = start
    while start <= end:
        if nums[start] > nums[max_index]:
            max_index = start
        start += 1
    return max_index

# test cases
nums = [44, 6,22, 2, 75, 1,36]
print(nums)
sort(nums)
print(nums)
