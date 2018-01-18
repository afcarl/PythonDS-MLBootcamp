# "** What is 7 to the power of 4?**"
7**4


#"** Split this string:**\n",
#"\n",
s = "Hi there Sam!"
print(s.split())


#"** Given the variables:**\n",
planet = "Earth"
diameter = 12742

#"** Use .format() to print the following string: **\n",
#"    The diameter of Earth is 12742 kilometers."


print("the diameter of {} is {} kilometers".format(planet, diameter))


#"** Given this nested list, use indexing to grab the word \"hello\" **"

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2][0])

#Given this nested dictionary grab the word \"hello\". Be prepared, this will be annoying/tricky

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])


#"** Create a function that grabs the email website domain from a string in the form: **\n",
#user@domain.com\n",
#So for example, passing \"user@domain.com\" would return: domain.com**"

def domainGet(domain):
    print(domain.split('@')[1])

domainGet("user@domain.com")


#Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.

def findDog(dogString):
    val = "dog" in dogString
    return val
findDog("Hey there is a dog over there")

#Create a function that counts the number of times the word \"dog\" occurs in a string. Again ignore edge cases.

def countDog(dogString):
    i = 0
    dogList = dogString.lower().split()
    for word in dogList:
        if word == 'dog':
            i += 1
    print(i)
    #return(i)
countDog("Hey look dog there is a dog in the dog park")


"""
"** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**

"    seq = ['soup','dog','salad','cat','great']\n",
"\n",
"**should be filtered down to:**\n",
"\n",
"    ['soup','salad']"
"""
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word:word[0] == 's', seq)))

"""
 Final Problem\n",
**You are driving a little too fast, and a police officer stops you. Write a function\n",
  to return one of 3 possible results: \"No ticket\", \"Small ticket\", or \"Big Ticket\". \n",
  If your speed is 60 or less, the result is \"No Ticket\". If speed is between 61 \n",
  and 80 inclusive, the result is \"Small Ticket\". If speed is 81 or more, the result is \"Big    Ticket\". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all \n",
  cases. **
"""




def func(speed, birthday):
    if birthday == False:
        no = 60
        small = 80
        if speed <= no:
            print("No Ticket")
        elif (speed >= no and speed <= small):
            print("Small Ticket")
        else:
            print("Big Ticket")
    else:
        no = 65
        small = 85
        if speed <= no:
            print("No Ticket")
        elif (speed >= no and speed <= small):
            print("Small Ticket")
        else:
            print("Big Ticket")
func(86, True)
