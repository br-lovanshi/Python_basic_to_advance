from data_structure.lists import List


class Solution:
    def searchRange(self, nums, target):
        return [firstPos(nums, target), lastPos(nums, target)]


def firstPos(nums, target):
    start = 0
    end = len(nums) - 1
    output = -1
    if len(nums) == 0:
        return -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            output = mid
            end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return output


def lastPos(nums, target):
    start = 0
    end = len(nums) - 1
    output = -1
    if len(nums) == 0:
        return -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            output = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return output


solution = Solution()
arr = [5, 7, 7, 8, 8, 10]
target = 8
output = solution.searchRange(arr, target)
print(output)
