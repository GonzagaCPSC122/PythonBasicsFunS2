import random

random.seed(0)

num_list = [] # list()
for i in range(20):
    random_number = random.randint(1, 10)
    num_list.append(random_number)

print(num_list)
# for item in sequence
for num in num_list:
    print(num, end=" ")
print()

num_list.sort()
print(num_list)

print("min:", num_list[0])
print("max:", num_list[-1]) # or len(num_list) - 1

# user_num = input("Enter a number: ")
user_num = 11
user_num = int(user_num)
print("your number is in the list:", num_list.count(user_num))

if user_num not in num_list:
    print("Sorry, your number is not here!")
else:
    # while user_num in num_list:
    for item in range(num_list.count(user_num)):
        num_list.remove(user_num)
print(num_list)

# 2D!!!!!
dataframe = [] # list()
for i in range(10):
    row = []
    for j in range(5):
        random_number = random.randint(1, 10)
        row.append(random_number)
    dataframe.append(row)
print(dataframe)

current_max = dataframe[0][0]
current_min = dataframe[0][0]

for row in dataframe:
    if max(row) > current_max:
        current_max = max(row)
    if min(row) < current_min:
        current_min = min(row)
print("max value:", current_max)
print("min value:", current_min)

user_num_count = 0
for row in dataframe:
    user_num_count += row.count(user_num)
print("user's number is in dataframe:", user_num_count)
 
removed = False
for row in dataframe:
    while user_num in row:
        removed = True
        row.remove(user_num)
print(dataframe)
if not removed:
    print("Sorry, your number is not here!")