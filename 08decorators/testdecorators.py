from time import sleep, time

def measure(func):
    def wrapper(*args, **kwargs):
        t = time() # starting time
        func(*args, **kwargs) # function call
        print(func.__name__, " Took :", time() - t)

@measure
def f3(sleep_time = 0.1):
    sleep(sleep_time) #pauses the program for the set amount of time

def f2(sleep_time = 0.1):
    sleep(sleep_time) # stops the execution for the given number of seconds

measure(f2(0.5))

f3(1)