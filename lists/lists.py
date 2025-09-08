n = int(input("Enter the number of elements"))

elements = []
while n:
    elements.append(int(input()))
    n -= 1

print(elements)

#check if all the elements are equal
#print true 
#otherwise false

currentValue = elements[0]
for i in elements:
    if i != elements[0]:
        print("false")
        currentValue = "a"
        break

if (currentValue != "a"):
    print("true")