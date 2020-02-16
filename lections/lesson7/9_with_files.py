f = open("test.txt")
f.close()

filepath = "test.txt"
with open(filepath) as f:
    for i in f.readlines():
        print(i)

