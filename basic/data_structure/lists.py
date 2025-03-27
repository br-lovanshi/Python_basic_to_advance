from collections import Counter


class List:
    name = [11, 2, 23, 3, 24, 5, 6, 6, 6]
    print(name)
    count = name.count(6)
    name.reverse()
    print(name)
    name.sort()
    print(name)
    name.append(9)
    print(name)
    name.pop(2)
    print(name)
    name.remove(6)

    nums = name.copy()
    print(nums)
    nums.insert(1, 55)
    print(nums)
    print(sum(nums))

    # collections.Counter (Similar to Java Map<K, Integer> for frequency count)

    print(Counter(nums))

    numbers = [1, 5, 2, 3]
    numbers.count(5)  # count the occurrence of value
    numbers.insert(99, 3)  # insert ele at specific index
    numbers.sort()  # sort the list asc
    numbers.reverse()  # reverse the list
    numbers.pop()  # remove the ele from specific index if index is provided else remove from last
    print(nums[2])
    print(numbers)

    def display(self):
        for num in self.nums:
            print(num)


list = List()
list.display()