# Comments in python begin with a single hashtag

x = 10 # Variables are declared and initialized without type keywords 
print(x) # A value can be printed out using the print function

x = 23 # Variables can be reassigned 
print(x)

y = None # Variables can be declared but not assigned to a value 
# by using the keyword "None" (null doesn't exist in python)
print(y)

y = 2

z = ( x + y)/x + (78%3) #usual mathematical operations supported 
print(z)

name = "bobby"
nameType = type(name) 
print(nameType) # This should indicate that the variable is a string (<class 'str'>)


age = 12
ageType = type(age)
print(ageType) # This should indicate that the variable is an integer (<class 'int'>)


height = 6.5
heightType = type(height)
print(heightType) #<class 'float'>

hasDate = False
hasDateType = type(hasDate)
print(hasDateType) #<class 'bool'>

comp = 7j 
compType = type(comp)
print(compType) # <class 'complex'>

# using fstrings for interpolation

message = f'Hi my name is {name} I am {age} years old'
print(message) # ‘Hi my name is bobby I am 12 years old'

# type casting to convert types
intHeight = int(height) # 6
strHeight = str(height) # '6'
floatHeight = float(intHeight) # 6.0

name  = input("Enter name: ") # reads input
print (name) # prints output

#correct
if 3 > 5:
  print("more") # The body of the if statement is this single line
else :
 print("less") # The body of the else statement is this single line

# Single line if-else statements can be written like this
# However this makes the code unreadable and is discouraged
if 3 > 5: print ("more")
else : print ("less")

# "else if" in python is written as elif
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70:
  print("A")
elif mark > 60: # Note the use of "elif"
  print("B")
elif mark > 50: # Note the use of "elif"
  print("C")
else:
  print("F") 

i = 1
while i < 10:
 print(i)
 i+=1
else:
 print("This is run when the loop condition is no longer met")

# iterating an iterable such as a list
list = ["bob", "sally", "john"]
for j in list:
 print(j)

# iterating between custom range an increment
for i in range(0, 10, 2):
 print(i)

 #basic function
def add(a, b):
    return a + b

def printPerson(name, age, height):
    print(name, age, height)

# you can specify arguments in any order if they are named
printPerson(age=12, name='bob', height=5)

#default arguments are used when they are not given in the function call
def sayHello(fname, lname='Smith'):
    print('Hello '+fname + ' ' + lname)

sayHello('John')

sayHello('Bill', 'Young')

# functions can return multiple values
def multiReturnFunc(a,b):
    return a+b, a-b, a*b, a/b

# You can assign multiple variables to the values being returned by the function
numSum, numDiff, numMult, numDiv = multiReturnFunc(10,5) 
print(numSum, numDiff, numMult, numDiv)

list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(list)
# negative indexing can access elements starting from the end
print(list2[-1])

# select a subset of a list
print(list2[2:4])

# gets the length of a list
print(len(list2))

#add items to list
list.append('item4')

#remove item from list
item4 = list.pop()

#copy list
list3 = list2.copy()

# list comprehension, lets you create new lists from existing lists

num = [ 1, 2, 3, 4]
doubled = [n*2 for n in num]
print(doubled) # [ 2, 4, 6, 8]
odd = [ n for n in num if n%2 == 1]
print(odd) # [ 1, 3]

# unpacking a list, lets you create variables from items in the list
num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)
# joining lists
num2 = [5, 6]
num3 = num + num2
print(num3) # [1, 2, 3, 4, 5, 6]

# copying lists
num4 = num2.copy()

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple); # ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple[0]); # ('apple')

data = [ 20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
 myset.add(num)

print(myset)# {0, 1, 2, 3, 32, 42, 10, 20}
num_unique = len(myset)