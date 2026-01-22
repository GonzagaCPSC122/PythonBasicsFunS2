"""
Questions from MA1
01: short circuiting, data structures, parameter vocab, dicts, file IO, 
sequence operators like slice, mutable parameters, interactive mode, value_map
02: bitwise operators, use of tuples/dictionaries, class methods, 
documentation, why foo? Information passing, how to know if a function returns a value?
"""
# interactive mode: see 01 zoom recording from last class

# documentation: see class coding standard document on Google Drive
# https://docs.google.com/document/d/1BuAUBNrJIRyKCAwvyw1GLT4Dk1IAI2tdHhFGiWGQkqA/edit?usp=drive_link

# why foo? see 02 zoom recording from last class

# short circuiting
def calculate_win_percentage(num, den):
    # assumes den != 0
    print("hello from calculate_win_percentage")
    return num / den 

# short circuiting
wins = 19
total_games = 0
# if total_games != 0 is False, and short circuits and calculate_win_percentage() is not called
if total_games != 0 and calculate_win_percentage(wins, total_games) >= 0.5:
    print("Win percentage is at least 50%")

# slice
candies = ["twix", "reeses", "oreos", "snickers", "m&ms", "starburst"]
print(candies[1:3]) # : is the slice operator. start index is inclusive
# end index is exclusive
# if you ever need a copy of a list, you can simply use the : with no start or end indices
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)
# slicing works with all sequences, including strings and tuples
word = "gonzaga"
print(word[:-3])
print(word[-3:])
print(word[::-1])

# mutable parameters (example: list aliasing)
def add_one_to_each_element(nums_list):
    # nums_list = []
    for i in range(len(nums_list)):
        nums_list[i] += 1

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
# list2 is a different list object from list1 (though they have the same values)
list1[0] = 10
print(list1, list2)
list3 = list1
# list3 is an "alias" for the same object that list1 refers to
list3[0] = 100
print(list1, list2, list3)
add_one_to_each_element(list1) # nums_list will be an alias for list1's object
print("after call:", list1, list2, list3)
# to make a copy of a 1D list: use the list copy() method
list4 = list1.copy() # "shallow" copy
list1[0] = 10000
print(list1, list2, list3, list4)
# python is pass by object reference
# functions with a reference to an object passed in
# can modify the object

# bitwise operators
num1 = 0b101 # 5
num2 = 0b011 # 3
# bitwise and
#        001 # 1
print(num1 & num2)
# bitwise or
#        111 # 7
print(num1 | num2) 

# how to know if a function returns a value (based on its call)?
# 1. used w/assignment operator
win_percentage = calculate_win_percentage(5, 10)
# 2. used in arithmetic expression
calculate_win_percentage(5, 10) * 100
# 3. uses as argument to another function call
print(calculate_win_percentage(5, 10))

# the remaining topics we will cover in next week or two

"""
Questions from MA2
practice with packing/unpacking, declaring and using global variables (and namespaces), when/why use generators, 
diff between dir/folder, why sudo dangerous, do python conveniences improve code readability, 
when use command line, can you avoid all errors, how does python find modules when you import them 
"""

# you use generators to save on memory (don't need to store all vals in a sequence, just
# generate one at a time as needed)
# I don't anticipate us making our own generators much in this class

# sudo is dangerous because you could break something system level on your machine
# such as deleting a file/folder the OS needs

# python conveniences can improve readability; but if you over use them you could start "code golfing" 
# (write code as short as possible), and that can get hard to read 
# (human visual spatial system uses spacing and consistency for processing)

# when use command line: when it is more efficient, 
# when it is easier/more helpful to debug/solve problems
# when you have to (e.g., there is no GUI way to accomplish your task)

# packing/unpacking
import math # typically at top of module

def compute_circle_circumference_area(radius: float) -> tuple[float]:
    circum = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circum, area

results = compute_circle_circumference_area(5.2)
print(results, type(results))
result1, result2 = compute_circle_circumference_area(5.2)
print(result1, result2)

# global vars and namespaces
print("before x declaration:", dir())
x = 3
print("after x declaration:", dir())
print()

def my_func():
    print("start of my_func():", dir())
    # print(x) # UnboundLocalError: local variable 'x' referenced before assignment
    x = 100
    print(x)
    print("end of my_func():", dir())

my_func()

def my_func2():
    print("start of my_func2():", dir())
    global x
    print("middle of my_func2():", dir())
    x = 10000
    print(x)
    print("end of my_func2():", dir())

print()
print("x before my_func2():", x)
my_func2()
print("x after my_func2():", x)
print()

try:
    infile = open("dne.txt")
    infile.close()
except FileNotFoundError as e: # catch specific error
    print("**********")
    print("FileNotFoundError:", e)
except Exception as e: # catch all errors with general Exception
    print("~~~~~~~~~")
    print("Exception:", e)
print("here")

# how python finds modules
# it looks in the "python path": current working directory, installed python packages
# to see your python path:
import sys
print(sys.path)