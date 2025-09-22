#measure the execution time of a funciton

#import time functions (Specific import)
from time import sleep, time

def f():
    sleep(0.3) # stops the execution for the given number of seconds

t = time() # return the number of seconds from 01/01/1970
f()
print("f took: ", time() - t)

# Let's create a function that takes another function
'''
def measure (func):
    t = time() # starting time
    func() # function call
    print(func.__name__, " took: ", time() -t)

    measure(f)
    ##measure(g)

#take a function with arguments)
'''

def f2(sleep_time = 0.1):
    sleep(sleep_time) # stops the execution for the given number of seconds

'''
def measure(func, *args, **kwargs):
    t = time() # starting time
    func(*args, **kwargs) # function call
    print(func.__name__, " Took :", time() - t)
    
measure(f2)
'''

#measure is a decorator

#@decorator 
#def f2(sleep_time = 0.1):
#    sleep(sleep_time) # stops the execution for the given number of seconds

def measure(func):
    def wrapper(*args, **kwargs):
        t = time() # starting time
        func(*args, **kwargs) # function call
        print(func.__name__, " Took :", time() - t)

@measure
def f3(sleep_time = 0.1):
    sleep(sleep_time) #pauses the program for the set amount of time

measure(f2(0.5))

f3(1)