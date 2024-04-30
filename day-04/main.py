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