# Create a lambda function

add = lambda x, y: x + y
#implement subtractiojn, multiplicaiton, and division
#check the division by 0

divide = lambda x, y: x / y if y!= 0 else "Error: Division by zero!"

#test the function
#create a list of tuples
inputs = [(10,5), (8,0), (14, 6)]

for x, y in inputs:
    print(f"Inputs: {x}, {y}")
    print(f"Addiction: {add(x,y)}")
    print(f"Division: {divide(x,y)}\n")

def create_mes(*args, **kwargs):
    #find the key in kwargs
    seperator = kwargs.get("Seperator", " ") #looks for a key value pair of seperator, default value is " "
    #code the rest of this later, presumably returns some seperated string afterwards

print(create_mes("a", "b", seperator = "-"))