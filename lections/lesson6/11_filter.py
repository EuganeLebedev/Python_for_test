numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [
    x
    for x in numbers
    if x % 2 == 0
]

print(even_numbers)

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

print(odd_numbers)


even_square_numbers = [
    x**2
    for x in even_numbers
]

print(even_square_numbers)

odd_sqare_numbers = list(map(lambda x: x**2, odd_numbers))

print(odd_sqare_numbers)

result = list(map(lambda x: x**3, filter(lambda x: x % 2 == 1, numbers)))

print(result)


result_sum = 0
for i in result:
    result_sum += i

print(result_sum)


from functools import reduce
result_sum_reduce = reduce(lambda x, y: x + y, result, 1000000)

print(result_sum_reduce)


sum_result = sum(result)
print(sum_result)








