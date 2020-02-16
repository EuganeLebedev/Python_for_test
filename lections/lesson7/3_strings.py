delta = 1000500
result = "Time: " + str(delta) # Time : 100500

old_result = "Time: " + "qweqwe" + ", second param: " + str(100500) + "-" + str(100500)
result =  "Time: {string}, second param: {number}-{number}".format(number=100500, string="qweqwe")

print(old_result)
print(result)

number = 100500
string = "qweqwe"
a = 1

res3 = f"Time: {string}, second param: {number}-{number}, {a}"
print(res3)

res4 = "Time: %s, second param: %s-%s" % (string, number, number)
print(res4)



