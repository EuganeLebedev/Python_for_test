''' pro dz '''

#not good
d = {'test': 1, 'test2': 2}
try:
	d['test3']
except KeyError:
	pass
	
#better,but still not good
value = d.get('test3', 1) #value == None

#idiomatic
'test3' in d #False
'test' in d # True

if 'test'in d:
else

# defaultdict
from collections import defaultdict
d = {}
d = dict()

dd = defaultdict(1)

dd['test'] += 1 #1

d.get('test',1) # same


''' list comprehensions '''

list comprehension
dict comprehension
set comprehension

input_list = [1,2,3,4,5,6]
#output_list = [1,4,9,16,25,36]

output_list = []
for i in input_list:
	output_list.append(i**2)
	
#next
employees = [ {'name': 'vasia', 'salary': '100500',}, {'name':'ivan', 'salary':10,}]

salaries = [] # 100500, 10
for employee in emplyees:
	salaries.append(employeees['salary'])

#	
total = sum(salaries) #100510

#
salaries = [
	employee['salary']
	for employee in employees
]
	
#
numbers = [
	i**2
	for i in range(10)
	]
# list comprehension
numbers = [
	'number' + str(i)
	for i in range(10)
	]

print(numbers)

# traditional way
numbers = []
for i in range(10):
	numbers.append('number' + str(i))

print(numbers)
	
#cycle in cycle
for i in range(100):
	for j in range(i*10):
		print('i: ' + str(i) + ', j: ' + str(j))
		
# 
numbers = [
	'number' + str(i)
	for i in range(10)
	for j in range(i*2)
]

print(numbers)

#
results = []
for i in range(10):
	for j in range(j, j*2):
		results.append(i + j)
		
# no more than one comprehansion!
result = [ 
	i + j
	for j in range(i, i*2)
	for i in range(10)
]

#
even_numbers = []
for i in range(100):
	if i % 2 == 0:
		even_numbers.append(i)

print(even_numbers)

#		
even_numbers = [
	i 
	for i in range(100)
	if i % 2 == 0
]

print(even_numbers)

#
even_numbers = [
	[i] 
	for i in range(100)
	if i % 2 == 0
]

print(even_numbers)

#
from math import sqrt

even_numbers = [
	sqrt(i) 
	for i in range(100)
	if i % 2 == 0
]

print(even_numbers)

#dict comprehension
d = {
	i: 'number ' + str(i)
	for i in range(100)
	}

print(d)

#pprint
from pprint import pprint

d = {
	i: 'number ' + str(i)
	for i in range(100)
	}

pprint(d)

# bad exapmle for comprehansion

employees = [ 'vasa pupkin', 'ivan ivanov', 'pert pertov']

employees_d = {
	employee.split(' ')[0]: employee.split(' ')[1]
	for employee in employees
	}
	
print(employees_d)
	
# traditional way
employees = [ 'vasa pupkin', 'ivan ivanov', 'pert pertov']

employees_d = {}

for employee in employees:
	names = employee.split(' ')
	employees_d[names[0]] = names[1]

print(employees_d)

#index error
employees = ['vasya\nPupkin', 'Ivan Dulin']

d = {}
for employee in employees:
	names = employee.split(' ') # \n
	d[names[0]] = names[1]
	
print(d)

#
#catch error
employees = ['vasya\nPupkin', 'Ivan Dulin']

d = {}
for employee in employees:
	names = employee.split(' ') # \n
	try:
		d[names[0]] = names[1]
	except IndexError:
		d[names[0]] = 'No value'
	
print(d)

''' random '''
import random

a = random.randint(1,2)
print(a)
print(a)

a = random.seed() # seed 
print(a)

# same numbers
import random

random.seed(100500)

for i in range(10):
	print(random.random())

#	
random
randint
seed
	
#no seed - different numbers for each run

import random

for i in range(10):
	print(random.random())
	

''' time and dates '''
21:06 Fri, 7
naive time 
aware time

GMT-0 # zero meredian time 
UTC # same 

UTC = 18:06

# today
import datatime

from datetime import date
from datetime import time
from datetime import datetime
from datetieme import timedelta


today = date( 2020, 2, 7)
print(today)

# min and max date
import datetime

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

	
dmn  = date.min
dmx = date.max
print(dmn)
print(dmx)

#
d2 = date.min

d2.replace(12)
d2.replace( day=12)
d2.replace(day = day)

d2.weekday()

d2.isoformat()
#

import datetime

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

d2 = date.min
print(d2)

d2 = d2.replace(12)
print(d2)

d2 = d2.replace( day=12)
print(d2)

#d2 = d2.isoformat()
print(d2)

d2.strftime("%d/%Y/%m")
print(d2)

# now, utcnow
import datetime

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = datetime(2020, 2, 7, 12, 6, 10)

print(today)

d = datetime.now()
print(d)

d = datetime.utcnow()
print(d)

#
import datetime

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

d = datetime.fromisoformat('2020-02-14 05:24.283')
print(d)

#
from datetime import datetime

d = datetime.fromisoformat('2020-02-14 05:24.283')
print(d)

d = datetime.strptime('21-02-2020','%d-%m-%Y')
print(d)


# posix time (unix time) 
now - 1970 = seconds #int

dt.timestamp()
print(dt)

#

d = datetime.fromtimestamp(1582232400.0)
print(d)

#
from datetime import datetime

t1 = datetime.utcnow()
print(t1)

t2 = datetime(2021, 2, 7, 18, 37, 59, 889487)

t3 = datetime.utcnow()
print(t2-t3

)

# error -- timedelta
from datetime import datetime
from datetime import timedelta

today = datetime.utcnow()

tomorrow = today + timedelta(day=1)

