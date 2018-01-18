#basic python refresher going over ints through lists
x = 'hello'
num = 12
name = 'Zach'
print('My number is {first} and my name is {second}'.format(first = num, second = name))

nest = [1,2,3,[4,5,['target']]]
print(nest)

#grab nested items
print(nest[3][0]) #gets 4
print(nest[3][2][0]) #gets 'target'
