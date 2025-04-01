class Arrays:
    def __init__(self, nums):
        self.nums = nums

    def reverse(self):
        i = 0
        j = len(self.nums) - 1
        while i < j:
            temp = self.nums[i]
            self.nums[i] = self.nums[j]
            self.nums[j] = temp
            i += 1
            j -= 1

    def find_value(self, target):
        try:
            return self.nums.index(target)
        except ValueError:
            return -1

    def find_min(self):
        # min = self.nums[0]
        # for i in self.nums:
        #     if i < min:
        #         min = i
        # return self.nums.index(min)
        if not self.nums:
            return None
        return self.nums.index(min(self.nums))


arr = Arrays([1, 4, 2, 7, 7, 9, 35, 3])
print(arr.nums)
# arr.reverse()
print(arr.nums)
print(arr.find_value(3))
print(arr.nums[arr.find_min()])