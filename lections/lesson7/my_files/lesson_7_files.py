my_file = open('./test_file.txt', mode='a')

#lines = my_file.readlines()
#print(lines)

line1 = my_file.readline()
print(line1)
line2 = my_file.readline()
print(line2)
my_file.write('qweqweqweqweqweqweqw')
my_file.close()

