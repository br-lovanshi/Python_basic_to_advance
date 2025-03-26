string = "Hello"
# for i in string:
# print(i)

for i in range(5):
    print(i)

list = ["Great", "Amazing", "Very nice"]
var = list[2]
print(var)
for name in list:
    print(name)

unique_value = {"monday", "tuesday", "monday", "wednesday"}
print(len(unique_value))
for day in unique_value:
    print(day)

for char in "python":
    if char == "h":
        continue
    print(char)

for i in range(1, 5, 2):  # start, end, skip
    print(i)

# iterate dictionary
student = {"name": "Brajesh", "age": 18, "is_passed": False}
for key, value in student.items():
    if key == "is_passed" and value is True:
        print("Congratulations")
    print(key, value)


# else loop
for i in range(4):
    print(i)
else:
    print("Loop finished successfully")

# while

x = 0
while x < 5:
    print(x)
    x += 1

