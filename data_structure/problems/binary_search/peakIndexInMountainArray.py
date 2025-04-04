from typing import List
class Solution:

    def order_agnostics_binary_search(self, nums, target, start, end):

        is_asc_sorted = nums[start] <= nums[end]

        if is_asc_sorted:
            while start <= end:
                mid = start + (end - start) // 2
                if target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    return mid
        else:
            while start <= end:
                mid = start + (end - start) // 2
                if target > nums[mid]:
                    end = mid - 1
                elif target < nums[mid]:
                    start = mid + 1
                else:
                    return mid

        return -1

    def peakIndexInMountainArray(self, arr: List[int], target:int) -> int:
       start = 0
       end = len(arr)-1
       while start < end:
           mid = start + (end - start) //2
           if arr[mid] < arr[mid+1]:
               start = mid + 1
           else:
               end = mid

       find_mid_target = self.order_agnostics_binary_search(arr, target, 0, start)
       if find_mid_target == -1:
           find_mid_target = self.order_agnostics_binary_search(arr, target, start, len(arr)-1)
       return find_mid_target

sol = Solution()
arr = [1,5,2,0]
print(sol.peakIndexInMountainArray(arr,2))