Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3]
>>> b=[1,2,3]
>>> for i in range(3):
	c[i]=b[i]+a[i]

Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    c[i]=b[i]+a[i]
NameError: name 'c' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c=[]
>>> for i in range(3):
	c[i]=b[i]+a[i]

Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    c[i]=b[i]+a[i]
IndexError: list assignment index out of range
>>> c
[]
>>> c[0,0,0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c[0,0,0]
TypeError: list indices must be integers or slices, not tuple
>>> c=[0,0,0]
>>> for i in range(3):
	c[i]=b[i]+a[i]

>>> c
[2, 4, 6]
>>> pop
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pop
NameError: name 'pop' is not defined
>>> pop
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pop
NameError: name 'pop' is not defined
>>> d=c.pop(4)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d=c.pop(4)
IndexError: pop index out of range
>>> d=c.pop(0)
>>> d
2
>>> c
[4, 6]
>>> del a,b,c,d
>>> a=[1,2,3,4,5]
>>> b=[1,2,3]
>>> c=[0,0,0,0,0]
>>> del c
>>> for i in range(5):
	c.append(i)=a[i]+b[i]
	
SyntaxError: can't assign to function call
>>> c=[0,0,0,0,0]
>>> for i in range(3):
	c[i]=a[i]+b[i]

>>> for i in range(4,5):
	c[i]=a[i]

>>> c
[2, 4, 6, 0, 5]
>>> r=[]
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	r.append(i)=c[i]+a[i]
	
SyntaxError: can't assign to function call
>>> for i in range(5):
	r=append.(c[i]+a[i])
	
SyntaxError: invalid syntax
>>> for i in range(5):
	r[i]=input('a[i]+c[i]')

a[i]+c[i]
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    r[i]=input('a[i]+c[i]')
IndexError: list assignment index out of range
>>> for i in range(5):
	r[i]=input(a[i]+c[i])

3
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    r[i]=input(a[i]+c[i])
IndexError: list assignment index out of range
>>> r
[]
>>> for i in range(5):
	r[i]=append.(a[i]+b[i])
	
SyntaxError: invalid syntax
>>> for i in range(5):
	r.append(a[i]+b[i])

Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    r.append(a[i]+b[i])
IndexError: list index out of range
>>> r
[2, 4, 6]
>>> for i in range(5):
	r.append(a[i]+c[i])

>>> r
[2, 4, 6, 3, 6, 9, 4, 10]
>>> v1=[1,23,45,67,1,24]
>>> v2=[2,45,5,1,222,99]
>>> for i in v1:
	b=v1[i]
	for i in v2:
		if b==v2[i]:
			print(v2[i])

Traceback (most recent call last):
  File "<pyshell#62>", line 4, in <module>
    if b==v2[i]:
IndexError: list index out of range
>>> for i in v1:
	b=v1[i]
	for i in v2:
		if b==v2[i]:
			print (b)

Traceback (most recent call last):
  File "<pyshell#64>", line 4, in <module>
    if b==v2[i]:
IndexError: list index out of range
>>> for i in range(5):
	b=v1[i]
	for i in range(5):
		if b==v2[i]:
			print (b)

1
45
1
>>> for i in range(6):
	b=v1[i]
	for i in range(6):
		if b==v2[i]:
			print (b)

1
45
1
>>> for i in v1:
	b=v1[i]
	for i in v2:
		if b==v2[i]:
			print (b)

			
Traceback (most recent call last):
  File "<pyshell#70>", line 4, in <module>
    if b==v2[i]:
IndexError: list index out of range
>>> def my_func():
	print("Hello!")

>>> my_func()
Hello!
>>> def my_func2(x1,x2):
	print(x1,x2)

>>> my_func2(5,9)
5 9
>>> my func2(6,9)
SyntaxError: invalid syntax
>>> def my_func2(x1,x2):
	print(str(x1),x2)

>>> my_func3(5,9)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    my_func3(5,9)
NameError: name 'my_func3' is not defined
>>> my_func3("rs",9)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    my_func3("rs",9)
NameError: name 'my_func3' is not defined
>>> def my_func2(x1,x2):
	print(str(x1)+x2)

>>> my_func2(2,"3")
23
>>> def my_func3(x1,x2):
	print(str(x1),x2)

>>> my_func3("rs",9)
rs 9
>>> def my_func4(x1="i m default"):
	print(x1)

>>> my_func4()
i m default
>>> my_func4(3)
3
>>> my_func4()
i m default
>>> 
my_func5=lambda (x1,x2):return(x1+x2)
SyntaxError: invalid syntax
>>> my_func5=lambda (x1,x2):(x1+x2)
SyntaxError: invalid syntax
>>> my_func5=lambda x1,x2:(x1+x2)
>>> print(my_func5(45,53))
98
>>> def my_func6(x1):
	t=x1.split(?)
	
SyntaxError: invalid syntax
>>> def my_func6(x1):
	t=x1.split("?")
	u=t[1].split("&")

>>> my_func6("in.search.yahoo.com/yhs/search?hspart=iba&hsimp=yhs-1&type")
>>> def my_func6(x1):
	t=x1.split("?")
	u=t[1].split("&")
	print(t)
	print(u)

>>> my_func6("in.search.yahoo.com/yhs/search?hspart=iba&hsimp=yhs-1&type")
['in.search.yahoo.com/yhs/search', 'hspart=iba&hsimp=yhs-1&type']
['hspart=iba', 'hsimp=yhs-1', 'type']
>>> my_func6('aaaa?bbbbbb?cccc&ddddd&')
['aaaa', 'bbbbbb', 'cccc&ddddd&']
['bbbbbb']
>>> def my_func():
	print("Hello!")

>>> b=my_func()
Hello!
>>> print (b)
None
>>> b
>>> b.append(my_func)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    b.append(my_func)
AttributeError: 'NoneType' object has no attribute 'append'
>>> def hcf(x1,x2):
	for i in range x1:
		
SyntaxError: invalid syntax
>>> def hcf(x1,x2):
	b=0
	for i in range(x1):
		if i%x1==0 and i%x2==0:
			if i>b:
				b=i

>>> hcf(4,6)
>>> def hcf(x1,x2):
	b=0
	for i in range(x1):
		if i%x1==0 and i%x2==0:
			if i>b:
				b=i
	print(b)

>>> hcf(4,6)
0
>>> def hcf(x1,x2):
	b=0
	for i in range(x1):
		if x1%i==0 and x2%i==0:
			if i>b:
				b=i
	print(b)

>>> hcf(4,6)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    hcf(4,6)
  File "<pyshell#138>", line 4, in hcf
    if x1%i==0 and x2%i==0:
ZeroDivisionError: integer division or modulo by zero
>>> def hcf(x1,x2):
	b=0
	for i+1 in range(x1):
		if x1%i==0 and x2%i==0:
			if i>b:
				b=i
	print(b)
	
SyntaxError: can't assign to operator
>>> def hcf(x1,x2):
	b=0
	i=1
	for i in range(x1):
		if x1%i==0 and x2%i==0:
			if i>b:
				b=i
	print(b)

>>> hcf(4,6)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    hcf(4,6)
  File "<pyshell#142>", line 5, in hcf
    if x1%i==0 and x2%i==0:
ZeroDivisionError: integer division or modulo by zero
>>> def hcf(x1,x2):
	b=0
	for i in range(x1-1):
		if x1%(i+1)==0 and x2%(i+1)==0:
			if i>b:
				b=i
	print(b)

>>> hcf(4,6)
1
>>> def hcf(x1,x2):
	b=0
	for i in range(x1):
		if x1%(i+1)==0 and x2%(i+1)==0:
			if i>b:
				b=i
	print(b)

>>> hcf(4,6)
1
>>> 
>>> def hcf(x1,x2):
	b=0
	for i in range(x1):
		if x1%(i+1)==0 and x2%(i+1)==0:
			if i>b:
				b=i+1
	print(b)

>>> hcf(4,6)
2
>>> hcf(11,121)
11
>>> hcf(4,8)
4
>>> calc(str(x1),x2,x3):
	
SyntaxError: invalid syntax
>>> def calc(str(x1),x2,x3):
	
SyntaxError: invalid syntax
>>> def calc(x1,x2,x3):
	if  x1=="add":
		return x2+x3
	else if x1=="subtract":
		
SyntaxError: invalid syntax
>>> def calc(x1,x2,x3):
	if  x1=="add":
		return x2+x3
	else if x1=="subtract":
		
SyntaxError: invalid syntax
>>> def calc(x1,x2,x3):
	if  x1=="add":
		print (x2+x3)
	elif x1=="subtract":
		print (x2-x3)
	elif x1=="multiply":
		print (x2*x3)
	elif x1=="divide"
	
SyntaxError: invalid syntax
>>> def calc(x1,x2,x3):
	if  x1=="add":
		print (x2+x3)
	elif x1=="subtract":
		print (x2-x3)
	elif x1=="multiply":
		print (x2*x3)
	elif x1=="divide":
		print (x1/x2)
	else print('wrong choice')
	
SyntaxError: invalid syntax
>>> def calc(x1,x2,x3):
	if  x1=="add":
		print (x2+x3)
	elif x1=="subtract":
		print (x2-x3)
	elif x1=="multiply":
		print (x2*x3)
	elif x1=="divide":
		print (x1/x2)
	else :
		print('wrong choice')

>>> calc("add",4,5)
9
>>> d=input('''input choice
               add-1
               subtract-2
               multiply -3
               divide -4''')
input choice
               add-1
               subtract-2
               multiply -3
               divide -41
>>> calc(d,4,6)
wrong choice
>>> d
'1'
>>> d=input('''input choice
               add-1
               subtract-2
               multiply -3
               divide -4''')
input choice
               add-1
               subtract-2
               multiply -3
               divide -4add
>>> calc(d,4,6)
10
>>> class car
SyntaxError: invalid syntax
>>> 
>>> class car
SyntaxError: invalid syntax
>>> 
=========== RESTART: C:/Users/Richa Sharma/Desktop/pythonclass.py ===========
Traceback (most recent call last):
  File "C:/Users/Richa Sharma/Desktop/pythonclass.py", line 11, in <module>
    car=Car("M","Red")
TypeError: object() takes no parameters
>>> 
=========== RESTART: C:/Users/Richa Sharma/Desktop/pythonclass.py ===========
Traceback (most recent call last):
  File "C:/Users/Richa Sharma/Desktop/pythonclass.py", line 11, in <module>
    car=Car("M","Red")
TypeError: object() takes no parameters
>>> 
