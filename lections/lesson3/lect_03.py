#LECT_03

#DZ

index =  0,1,2,3,4
l = 	[1,2,3,4,5]
-index = -3,-2,-1

#q1

x = (1,2,3)

alph, beta, gama = x
print(alpha)
print(beta)
print(gama)

beta, gama = x
error = too many values too unpack


#q2

x = (1,2,3,[5,6,7]

x[3].append(7)
print(x)

l.insert(1, 100500)
x[3].insert(1, 100500)

#pro dz
l = list(range(n)) # list?

4 % 2 == 0

3 % 2 == 1

a = 4

b = 3

c = a % b

c == 0

False

if c == 0 (False)

else

#dz 

return (,) 
return (x,)
return(x1,x2)

string ?


#example


#dz

l = [] # norm (low skill)

def fibb(n):
	l.apppend(100500)
	
print(l)

# example dz

def func():
	return 1
	a = 1 + 2 # no!
	return 2 # !
	
#e2

def func():
	pass
	
	
#e3

str
dict
list

None 

a = None #default value

b = a + 1 # error

	
a = None

print(a)

def func():
	print(123)
	
a = func()
print(a)


#e3
l = [1,2,3]

print(l)
l.append(100500)
print(l)

l = None

l.append(100500) #attribute error

#e4
a = None
if a is None:
	print('This is None')
else:
	prin(a)
	
#e5
def calc(a,b,c):
	if d < 0:
		return None
		
result = calc(1,2,3)

if result is None: 
	print('no')

#e6 

a = '123'
b = int(a)

a = '123'
b = int(a)

c = 22.65
b = int(c)

print(b) # 22

f = float(b)

print(f) # 22.0

s = str(f)

print(s)

a = int(s) # error

a = int('100500')
a +=1 
print(a)

# e 7

int + float = float

# e 8
a = [1,2,3] + [4,5,6] 
print(a)

# e9
a = None
print(a is None)
isinstance(a, type)	#homework!!

print(isinstance(123, int))

print(type(a))


# e 10
for i in range(100):
	if i < 15:
		print(i)
	else:
		break
	
# e 11

for i in range(100)
	if i%2 ==0:
		continue:
	
	print(i)


# e 12
b = 4
a = None	

if b % 2 == 0:
	a = "Even"
else:
	a = "Odd"
	
a = "even" if b % 2 == 0 else "Odd" #same

print(a)

# e 13
print('b' > 'B') # True


		# Part 2
		
1 / 0
ZeroDivisionError

Traceback


# e1
SyntaxError

a = (int) 4.0

# e2
RuntimeError
1 / 0

None.append
AtributeError

# e3
UTF-8
с = 'c'
print(c)
print(с) #rus - NameError

# e4

error = NameError("my custom exception")


def run(a):
	if a % 2 == 0:
		raise error
	else:
		print(a)

run(44)

#e5
error = NameError("my custom exception")


def run(a):
	if a % 2 == 0:
		raise error
	else:
		print(a)

try:
	run(44)
except:
	pass
finally:	#optional
	pass

#e6
error = NameError("my custom exception")

def run(a):
	if a % 2 == 0:
		raise error
	else:
		print(a)

try:
	run(44)
except: 
	print("error")

#e7

error = TypeError("my custom exception")

def run(a):
	if not instance(a,int):
		raise error
	else:
		print(a)

try:
	run(44)
except NameError:  
	print("error")

#e8
error = TypeError("my custom exception")

def run(a):
	if not instance(a,int):
		raise error
	else:
		print(a)

try:
	run(44)
except NameError:  
	print("error")

except TypeError:
	print(123)
	
#e9

error = TypeError("my custom exception")

def run(a):
	if not instance(a,int):
		raise error
	else:
		print(a)

try:
	run(44)
except (NameError, TypeError):  
	print("error")


#e10

error = TypeError("my custom exception")

def run(a):
	if not instance(a,int):
		raise TypeError("my custom except")
	else:
		print(a)

try:
	run(234)
except (NameError, TypeError) as e:  
	if isinstance(e, TypeError):
		print('type')
	else:
		print('name')
		
#e11
error = TypeError("my custom exception")

def sqrt(a):
	return a**0.5

sqrt("asfd;lj")


try:
	sqrt(234)
except (NameError, TypeError) as e:  
	if isinstance(e, TypeError):
		print('type')
	else:
		print('name')
		
#e12
a = input('input number: ')

try:
	int_a = int(a)
except ValueError:
	print('!')
	
#e13
def func2(a):
	if not isinstance(a, int):
		raise ValueError()
	
	print(a**2)

def func1(a):
	try:
		func2(a)
	except ValueError:
		func2(int(a))

func1("3242342")



 
	
















 







