# Python Crash Course Part 4
# map()

#def times2(var):
#    return var*2

def times2(var):return var*2 # this is the same as the above traditional function

seq = [1,2,3,4,5]
# can use for loop to apply times2() on every element of seq, or we can use map()

list(map(times2, seq))
print(list(map(times2, seq)))

# lambda

lambda var:var*2 # saves you time from defining a function

print(list(map(lambda num:num*3, seq)))


# filter

# filter takes in a lambda expression or function that returns a boolean value, and then returns only the true values
print(list(filter(lambda num:num%2 == 0, seq))) # This returns only the even numbers in seq

s = 'hello my name is Zach'

s.upper()
print(s.upper())

# split() splits a string on the whitespace into a list, or whatever the args is

print(s.split())
tweet = 'Go Sports! #Sports'

print(tweet.split('#'))
hashtags = tweet.split('#')[1]
print(hashtags)


d = {'k1': 1, 'k2':2}

print(d.keys())


lst = [1,2,3]
lst.pop()

#pop() permanently "pops-off" the last item of a list, or whatever the args is
print(lst)
lst.append('new')
lst.pop(0)
print(lst)

# Tuple unpacking
x = [(1,2), (3,4), (5,6)]

for a,b in x:
    print(a)
