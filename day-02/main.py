# int 300,200,100
# float 3.2,1.0,2.0
# str 'girish','surish','hatrish'
"""-------------------------------------"""
# list
# dict
# tuple
# set
# bool

"""-------------------------------------"""

# Number In Python
# basic math in py
print("add 2+1 = ", 2+1)
print("sub 2-1 = ", 2-1)
print("mul 2*1 = ", 2*1)
print("div 2/1 = ", 2/1)
print("mod 7%4 = ", 7 % 4)


print(2*3+4*5)
print((2*3)+(4*5))


# variable assignment

my_dog = 2
myMemo = 23
print(my_dog)
print(myMemo)

# dynamic assignment

my_dog = "doggy poggy"
print(my_dog)

# type()

print(type(my_dog))
print(type(myMemo))


print()
print()
print()
print()
print()

a = 2
b = 2.0
c = "string"
print(type(a))
print(type(b))
print(type(c))

print()
print()
print()

p = 1000
roi = 0.1
t = 3
si = (p*roi*t)/100
print("simple intrest", si)


print()
print()
print()

# string

myStr = 'this me sreephaneesha'
print(myStr)
print(len(myStr))

print()
print()
print()

str1 = "sreephaneesha is a good \"boy\" \n he is also a good human \t that's it"
print(str1)
print(len(str1))

print()
print()
print()

str2 = "hello"
print((str2))
print(len(str2))

print()
print()
print()

str6 = "Hello"
print(str6[0])
print(str6[1])
print(str6[2])
print(str6[3])
print(str6[4])
print(str6[-1::-1])


print()
print()
print()

abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc[2:])
print(abc[:3])  # stop index will not include tht number
print(abc[3:12])
print(abc[1:3])
print(abc[::3])
print(abc[::-1])  # ----> reversing a string

print()
print()
print()

# string properties

'''
name='sree'
name[0]='r'
print(name) # TypeError: 'str' object does not support item assignment
'''

name = 'sree'
mname = 'phaneesha '
lname = 'kanugovi'
print(name+mname+lname)
print(mname*10)

print()
print()
print()

x = "heLLo world"
print(x.upper())
print(x.lower())
print(x.split())
print(x.zfill(22))

print()
print()
print()

# print formatting

myname = 'sreephaneesha kanugovi'
print('Hello '+myname)
print("hello {}".format(myname))
print(f"Hello {myname}")  # new and easy

mynum = 100/777
print(f"my num is {mynum:1.3f}")
print(f"my num is {mynum:1.2f}")
print(f"my num is {mynum:30.4f}")

print()
print()
print()

name = 'sreephaneesha kanugovi'
age = 18
print(f"Hello {name} your age is \033[31m{age}")

print()
print()
print()

# List

list1 = [1, 2, 3, 4, 'sree', 'phaneesh']
list2 = [6, 7, 8, 9, 'k', 'kaddi']
print(len(list1))
print(list1[1:])

newlist = list1+list2
print(newlist)

newlist[4] = 'kodi'
print(newlist)

newlist.append("python3")
print(newlist)

newlist.append("javascript")
print(newlist)

newlist.pop()  # return the removed item
print(newlist)

newlist.pop(2)  # return the removed item at the given index
print(newlist)

newlist = [2, 1, 3, 4, 5, 9, 6, 7, 8]
newlist.sort()
print(newlist)

newlist = ['a', 'e', 'i', 'i', 'u']
newlist.sort(reverse=True)
print(newlist)

newlist = ['a', 'e', 'i', 'i', 'u']
newlist.sort()
print(newlist)

print()
print()
print()

# dict
myDict = {
    'key1': 'value1',
    'key2': 'value2',
    'apple': 1.99,
    'egg': 2.559,
    'chuck': 4.99,
    'bucks': 4.99,
    'k1': [1, 2, 3, 4, 5],
    'l': [22, 44, 55, 66, 77]
}

print(myDict['key1'])
print(myDict['bucks'])
myDict['k1'] = "strings"
print(myDict.keys())
print(myDict.values())
print(myDict.items())

print()
print()
print()

# tuples
tuple1 = (1, 2, 3, 4, "string", 1, 1, 'a', 1, 1, 1, 'a')
print(len(tuple1))
print(type(tuple1))
print(tuple1[1])
print(tuple1.count(1))
print(tuple1.index('a'))
''' tuple1[0]='title' # TypeError: 'tuple' object does not support item assignment '''

print()
print()
print()
print()

# sets
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
set2 = set()
print(set1)
print(set2)

print()
print()
print()
print()

# bools
isUser = True
isLoggedIn = False
print(type(isUser))
print(isUser)
print(isLoggedIn)

print()
print()
print()

# Files

file = open('/home/spk/python3-Zero-To-Hero/day-02/test.txt')
file.seek(0)
lines = file.read()
file.seek(0)
linesarray = file.readlines()
print(lines)
print(linesarray)
file.close()

print()
i=None
with open('/home/spk/python3-Zero-To-Hero/day-02/test.txt',mode='a') as myfile:
    print(myfile.write(f"\nHello writter by python {i}"))

with open('pythontxt.txt',mode='w') as f:
    print(f.write("Hello writter by python into file"))

with open('pythontxt.txt',mode='r') as f:
    print(f.readlines())


print()
print()
print()

