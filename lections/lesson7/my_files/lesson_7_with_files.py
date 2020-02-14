f = open('test_file.txt')
f.close()

with open('test_file.txt') as f:
    lines = f.readlines()
    print(lines)
