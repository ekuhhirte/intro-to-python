#function that creates a method

def create_message(prefix, *args):
    s = " "
    for arg in args:
        s += str(arg) + " "
    print(s)
    pass

#calls a function

create_message("Status", "Temp", 25, "Degree")