class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p = person("Ram", 26)
p.display()


class Student:
    def __init__(self):
        print("Default constructor")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Constructor is called")

    def avg_marks(self):
        count = 0
        for mark in self.marks:
            count += mark
        print("Avg marks of ", self.name, "is", count / len(self.marks))


# find the avg marks of student
s1 = Student("Brajesh Lovanshi", [99, 84, 88])
print(s1.marks)
s1.avg_marks()
s1.name = "Ram"
s1.avg_marks()
