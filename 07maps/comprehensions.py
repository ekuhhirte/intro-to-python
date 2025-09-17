# Create a funciton that reutrns a list of cubes for odd number in a given range

def cubes_of_odds(start,end):
    return [x**3 for x in range(start, end+1)]

print(cubes_of_odds(1,10))
#print(cubes_of_odds(1,1000))

#Create a function that creates a list of uppercase words longer than 3 characters

def long_upper_words(words):
    #return map(str.upper, filter(len( >3, words)) doesn't work because you can't get the lenth of it
    return [word.upper() for word in words if len(word) > 3]

words = ["Polytechnic", "COP", "oop", "StudEnt"]
print(long_upper_words(words))