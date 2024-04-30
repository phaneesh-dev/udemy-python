# if elif else

if True:
    print("hello if else")

print()

if 2>2:
    print("is greater")
else:
    print("small")


print()
print()
print()


isValid=False
if isValid:
    print("yes its valid")

else:
    print("not valid")

print()
print()
print()

age=11
if age>18:
    print("vote is eligible")
elif age==18:
    print("Go to Apply votting card")
else:
    print("You are ineligible")

print()
print()
print()

# for loops
'''
for variable in itrable:
    code
'''
my_list=[1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    if i%2==0:
        print(f"{i} even")
    else:
        print(f"{i} odd")
 
print()
print()
print()

for i in my_list:
    print('i'*i)

print()
print()
print()

sum=0
for i in my_list:
    sum+=i
    print(sum)

print()
print()
print()

for c in "sreephaneesha":
    print(c)

print()
print()
print()


# tuple unpacking
list1=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(12,13)]
for i,j in list1:
    print(f"{i} <--> {j}")

print()
print()
print()
print()


# while loops
'''
while condition is True:
    /* code */
'''

x=10
while x<10:
    print(f"{x}")
    x+=1
else:
    print("x is no longer less than 10")

print()
print()
print()


# useful Opratorss


for i in range(0,11,2):
    print(i)

print()
print()
print()


for c in enumerate('abcd'):
   print(c)

print()
print()
print()

my_list=[1,2,3,4,5,6,7,8,9]
my_list1=['a','b','c','d','e','f']

for item in zip(my_list,my_list1):
    print(item)

print()
print()
print()

print([1,2,3] in [1,2,3])
print(2 is 4)

print()
print()
print()

from random import shuffle,randint
mylist=[1,2,3,4,5,6,7]
shuffle(mylist)
print(mylist)

print()
print()
print()

print(randint(1,100))

print()
print()
print()

name=input("enter name: ")
print(name)

print()
print()
print()

# list compreshension

mylist=[i for i in name]
print(mylist)

print()
print()
print()

my_list=[i**2 for i in range(11)]
print(my_list)

print()
print()
print()

my_list=[i**2 for i in range(11) if i%2==0]
print(my_list)

print()
print()
print()
print()

result=[x if x%2==0 else 'odd' for x in range(11)]
print(result)

