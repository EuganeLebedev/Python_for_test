delta = 100500
result = "Time" + str(delta)

result = "Time {}, second param: {}".format(100500, 'qwe')
print(result)

result = "Time {string}, second param: {number}".format(number=100500, string='qwe')
print(result)


number = 100500
string = 'qwertyuiop'

result3 = f"Time: {string}, second param: {number} - {number}"
print(result3)
