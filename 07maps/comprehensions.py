# Create a funciton that reutrns a list of cubes for odd number in a given range

def cubes_of_odds(start,end):
    return [x**3 for x in range(start, end+1)]

print(cubes_of_odds(1,10))