# https://leetcode.com/problems/find-in-mountain-array/
class Solution:
    def peakIndex(arr):
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
