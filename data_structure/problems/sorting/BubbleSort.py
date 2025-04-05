def sort(nums):
    """
    Sorts a list of numbers using the bubble sort algorithm.
    
    :param nums: List of numbers to be sorted
    :return: Sorted list of numbers
    """
    n = len(nums)
    for i in range(n):
        is_swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j+1]:
                swap(nums, j, j + 1)
                is_swapped = True
            
        if is_swapped == False:
            break


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

# test case
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", nums)
    sort(nums)
    print("Sorted array:", nums)
# Time Complexity: O(n^2)
# Space Complexity: O(1)    
# problem link: https://takeuforward.org/data-structure/bubble-sort-algorithm/

"""
🎯 When to Use Bubble Sort?
Small inputs (≤ 100 elements).
Educational purposes (learning sorting).
Almost sorted arrays (Best case O(n)).
For larger datasets, Quick Sort or Merge Sort 
"""