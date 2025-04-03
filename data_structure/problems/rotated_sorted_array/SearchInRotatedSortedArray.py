class Solution:
    def find_pivot(self, nums)->int:
       start, end = 0, len(nums)-1
       if nums[start] < nums[end]:
           return -1
       
       while start <= end:
           mid = start + (end - start) // 2
           if nums[mid] < nums[mid - 1]:
               return mid
           elif nums[mid] > nums[end]:
                start = mid + 1
           else:
                end = mid - 1
       return start
         
           
           
    def binary_search(self, nums, left: int, right: int, target: int) -> int:    
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Example usage:
nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
pivot = solution.find_pivot(nums)

if pivot == -1:
    print(solution.binary_search(nums, 0, len(nums) - 1, target))
elif nums[pivot] == target:
    print(pivot)
elif target >= nums[0]:
    print(solution.binary_search(nums, 0, pivot - 1, target))
else:
    print(solution.binary_search(nums, pivot, len(nums) - 1, target))

# This function searches for a target value in a rotated sorted array.
# It first finds the pivot point where the array is rotated,
# and then performs a binary search in the appropriate half of the array.
# The function has a time complexity of O(log n) and a space complexity of O(1).
# The function takes an array and a target value as input,
# and returns the index of the target value if found, or -1 if not found.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Problem Link:
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/