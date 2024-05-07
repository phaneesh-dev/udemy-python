# methods in python
mylist=[1,2,3,4]
mylist.append(5)
mylist.pop()
print(mylist)

mylist.insert(2,6) # insert 6 at index 2
print(mylist)

print()
print()
print()

# functions in python
def myfunc1():
    print("Hello")

def myfunc(name):
    print("Hello "+name)

myfunc1()
myfunc("Harsh")
myfunc("Aman")
myfunc("Amazon Q")


print()
print()
print()

''' ''' # is a multiline comment `docstring`

# return keyword in python
def add(num1,num2):
    return num1+num2

sum=add(2,3)
print(sum)

# basics of python
# variables in python
def say_hello():
    print("Hello")

say_hello()
# print(say_hello())

print()
print()
print()

def say_hello(name="spk"):
    print("Hello "+name)

say_hello("Harsh")
say_hello("Aman")
say_hello()

print()
print()
print()

def add(num1,num2):
    return num1+num2

sum=add(2,3)
print(sum)


print()
print()
print()
print()

def even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(even(22212123))

print()
print()
print()


new_even_list=[]
def evenList(numlist):
    for num in numlist:
        if num%2==0:
            new_even_list.append(num)
    return new_even_list
        
print(evenList([1,2,3,4,5,6,7,8,9]))


print()
print()
print()

# tuple unpacking using fucntion

stock_prices = [("apple", 200), ("orange", 100), ("mango", 300)]

def print_stock_prices(stock_prices):
    for item,price in stock_prices:
        return {item,price}
    
print(print_stock_prices(stock_prices))

print()
print()
print()


import random
exam=[1,2,3,4,5,6,7,8]
random.shuffle(exam)
print(exam)

print()
print()
print()

# *args **kwargs

def myfunc1(a,b):
    return (__builtins__.sum((a,b))*0.05)
print(myfunc1(40, 60))

print()
print()
print()

def myfunc2(*args):
    return __builtins__.sum(args)*0.05

result=myfunc2(40, 60, 100, 200,300,400)
print(result)

print()
print()
print()

def myfunc1(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not find any fruit here")

myfunc1(fruit="apple", veggie="lettuce")

print()
print()
print()

def myfunc1(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['fruit']}")
myfunc1(10, 20, 30, fruit="orange", food="eggs", animal="dog")

print()
print()
print()

# map
def square(num):
    return num**2

my_nums=[1, 2, 3, 4, 5]
map(square, my_nums)
print(list(map(square, my_nums)))

print()
print()
print()


# filter 
mynums=[1, 2, 3, 4, 5,6,7,8,9,10,11,12]
def check_even(num):
    return num%2==0
print(list(filter(check_even,mynums)))

print()
print()
print()

# lambda

sqr=lambda x: x**2
print(sqr(5))

print()
print()
print()

# product of number in 2 lis
num1=[1, 2, 3, 4]
num2=[5, 6, 7, 8]
print(list(map(lambda x,y:x*y,num1,num2)))

print()
print()
print()

x=25
def printer():
    x=50
    return x
print(x)
print(printer())
print(x)

print()
print()
print()

def huu():
    global x;x = 123
    print(x)

huu()
print(x)