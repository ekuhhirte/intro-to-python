from nicegui import ui

#functions
def generateHash():
    userInput = input_field.value.strip() #.value returns the value currently saved in that input field
    hash = 0x9E3779B1 #stores the hash as a hexadecimal number

    for char in userInput:
        hash = hash ^ ord(char) # performs XOR bitwise operation on the hash and the character code and saves it as the new value
        hash *= 0x517CC1C7 #updates the hash by multiplying it by 0x517CC1C7
        hash = hash & 0xFFFFFFFF #keeps only the lowest 32 bits byt applying bitwise AND with 0xFFFFFFFF
    
    hash = hash ^ len(userInput) # applies bitwise XOR with the length of input

    hashoutput.text = f"Hash Value: {hash}" #updates the hashoutput label to store the new hash everytime the function is run
    


#Page layout and basic button
with ui.card().classes("h-65 w-120"):
    ui.label("Hashing").style("color: green; font-size: 40px")
    input_field = ui.input("Enter Message")
    hashoutput = ui.label("Hash Value:").style("color: black; font-size: 20px")
    ui.button("GET HASH", on_click = generateHash) #calls the generate hash function which grabs its own input and displays output without anything else needed


ui.run(title = "HW7_GUI") #actually runs the UI code, title sets the website title to whatever string is there