#test

words = ["python", "c", "java"]

#return a new list with capitalized words

#Capitalized_Words = map(str.upper, words)
#print(Capitalized_Words)

print(list(map(str.upper, words)))

texts = ["   Hello   World   ", "Python   Programming", "   Data   Science   "]

john = map(lambda s: ''.join(s.split()), texts)

print(list(john))

#filtering even numbers

numbers = [1,2,3,4,5,6]

evens = filter(lambda x: x%2 == 0, numbers)
print(list(evens))

odds = filter(lambda x: x%2 != 0, numbers)
print(list(odds))

squares = [x**2 for x in range(5)]
print(squares) # Output = 0,1,4,9,16

evens = [x for x in range(10) if x%2 ==0]
print(evens) # oiutput should be only the evens between 0 and 9 inclusive.

even_squares = {x: x**2 for x in range(10) if x%2 == 0}
print(even_squares)