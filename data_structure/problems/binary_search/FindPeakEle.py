# https://leetcode.com/problems/find-peak-element/description/?envType=problem-list-v2&envId=m5uiyrgv
# https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1594214185/?envType=problem-list-v2&envId=m5uiyrgv
# https://leetcode.com/problems/find-in-mountain-array/

def find_peak(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


arr = [5,7]
print(find_peak(arr))
