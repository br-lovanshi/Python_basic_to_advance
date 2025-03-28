class Sets:
    set = {1,5,2,5,5,5,2,1,6,1}
    print(set)
    set.pop()
    new_set = set.union({2,3,5,6,99})
    print(new_set)
    new_set.add(7)
    new_set.remove(5)
    intersection_set = new_set.intersection({4,2,6,7,8,9})
    print(intersection_set)

    def display(self):
        for num in self.set:
            print(num)


set = Sets()
set.display()