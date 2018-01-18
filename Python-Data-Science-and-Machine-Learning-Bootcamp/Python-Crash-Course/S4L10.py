#Python Crash Course Lesson 2

#Dictionaries

d = {'key1': 'value', 'key2' : 123}
# dicitonaries take in key:value pairs.
print(d['key2'])

dict2 = {'key1':'value', 'key2':[1, 2, 3]}
print(dict2['key2'][1]) #grabs 2

my_list = dict2['key2']
print(my_list[1]) #this does the same thing, but is more verbose


dd = {'k1':{'innerKey':[1,2,3,4]}}
print(dd['k1']['innerKey'][1]) #grabs 2

inner_dict = dd['k1']['innerKey']
print(inner_dict[1]) # also grabs 2

# Tuples

my_list = [1,2,3]
t = (1,2,3)
print(my_list[0])
my_list[0] = 'NEW'
print(my_list[0])

# Tuples are immutable
#t[0] = 'NEW'


# Sets only return unique values
s = {1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3}
s.add(5)
print(s)

# Equalities
print(1 >= 3)
print( 1 != 2)

#Logic Operators

print(1<2 and 2<3)
print((1<2) and (3<2))
print((1<2) or (3<2) or (1==1))


# if, elif, else
if 1<2:
    print('Hey that condition is true!')

if 3<2:
    print('Hey that condition is true!')
else:
    print('That condition is false!')

if 3<2:
    print('First')
elif 4>3:
    print('Second')
else:
    print('Third')
