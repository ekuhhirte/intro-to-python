from nicegui import ui

#functions



#Page layout and basic button
with ui.card().classes("h-65 w-120"):
    ui.label("Hashing").style("color: green; font-size: 40px")
    input_field = ui.input("Enter Message")
    hashoutput = ui.label("Hash Value:").style("color: black; font-size: 20px")
    ui.button("GET HASH")


ui.run(title = "HW7_GUI") #actually runs the UI code, title sets the website title to whatever string is there