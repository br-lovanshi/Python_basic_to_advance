def pattern1(num):
    for i in range(num+1):
        for j in range(i+1):
            print("*", end=" ")
        print()

print("Pattern 1")
pattern1(5)