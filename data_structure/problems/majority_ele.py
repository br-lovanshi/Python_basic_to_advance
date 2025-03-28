from typing import List


def majorityElement(nums: List[int]) -> int:
    nums.sort()
    print(nums)
    n = len(nums)
    return nums[n // 2]


class Solution:
    pass


s = Solution()
print(majorityElement([1, 5, 5, 5, 8, 5, 3, 9, 0]))
