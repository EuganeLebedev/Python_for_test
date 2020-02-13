l = [1,2,3,4,5]

def func(a):
    a.append(100)
    a = ["qwe", "zxc"]
    a.append(5000)
    return a

print(l)

b = func(l)

print(b)
print(l)

