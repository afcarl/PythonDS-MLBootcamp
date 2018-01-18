# Python Crash Course Part 3

seq = [1,2,3,4,5]

# For Loop
for item in seq:
    print(item)

for item in seq:
    print('item')

# While Loop

i = 1

while i < 5:
    print('i is: {}'.format(i))
    i += 1

# Range

range(0,5)
for x in range(0,5):
    print(x) #prints values 0, 1, 2, 3

list(range(10)) # Creates a temporary list from 0 up to but not including 10


x = [1,2,3,4]
out = [] # empty list

for item in x:
    out.append(item**2)
print(out)

# List Comprehension

print([num**2 for num in x]) # produces the same result as the above for-loop


# Functions

def my_func(param='Default Name'):
    print('Hello ' + param)

my_func("Zach")
my_func()

def square(num):
    """
    Here is a documentation string, basically
    a multi-line comment
    """
    return num**2
output = square(3)
print(output)
