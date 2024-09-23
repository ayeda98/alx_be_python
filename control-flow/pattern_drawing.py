length = int(input("Enter the size of the pattern: "))
a = 1
while a <= length:
    for i in range(length):
        print("*", end="")
    print()
    a+=1