def binary_search(arr:int, start:int, end:int, target) -> int:
    while start <= end:
        try:
            mid = start + (end - start)//2
            if arr[mid] > target:
                end = mid-1
            elif arr[mid] < target:
                start = mid+1
            else:
                return mid
        except IndexError:
            end = mid-1

    return -1


def find_ranges(arr: int, target: int) -> int:
    start = 0
    end = 1
    while True:
        try:
            if target <= arr[end]:
                break
            end *= 2
        except IndexError:
            break

    return binary_search(arr, start, end, target)


arr = [1, 3, 5, 6, 10, 15, 19, 29, 59, 74, 355, 994, 3244]
target = 9944
print(find_ranges(arr, target))

# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/