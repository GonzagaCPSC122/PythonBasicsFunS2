a = [1, 2, 3]
b = a # b becomes an alias to the same object a refers to
b[1] = 0
print(a)
print(b)

my_string = "a,b,c"
substrings = my_string.split(",") # returns reference of type list[str]
print(substrings, type(substrings), type(substrings[0]))

for i in range(2, 42, 2): # range: inclusive of start value, exclusive of stop value
    print(i, end=" ")
print()

def count_lines(filename: str) -> int:
    infile = open(filename)
    num_lines = len(infile.readlines())
    infile.close()
    return num_lines

num = count_lines("english.txt")
print("num lines in file:", num)
