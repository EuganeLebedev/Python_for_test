with open("test2.txt") as f:
    for i in f:
        print(i)

with open("test2.txt") as f:
    for i in f.readlines():
        print(i)
