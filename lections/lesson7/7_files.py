f = open("./test.txt")

l1 = f.readline()
print(f"Line 1: {l1}")
l2 = f.readline()
print(f"Line 2: {l2}")
l3 = f.readline()
print(f"Line 3: {l3}")
l4 = f.readline()
print(f"Line 4: {l4}")
l5 = f.readline()
print(f"Line 5: {l5}")
l6 = f.readline()
print(l6 == "")
print(f"Line 6: {l6}")
f.close()
