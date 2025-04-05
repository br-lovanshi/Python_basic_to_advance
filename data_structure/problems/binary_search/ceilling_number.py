# https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

def ceiling_num(nums, x):
    output = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > x:
            output = mid
            end = mid - 1
        elif nums[mid] < x:
            start = mid + 1
        else:
            output = mid
            break
    return output


nums = [1, 2, 8, 10, 10, 12, 19]
x = 11
print(ceiling_num(nums, x))

# https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=SUBMISSION
