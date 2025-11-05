from nicegui import ui





# Create a greeting

#-----------------------GREETING---------------------------



def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}"
    ui.notify(msg)




#--------------------COUNTER----------------------------
#Create a counter
class State:
    count = 0



def add_one():
    State.count += slider.value
    count_label.text = f"Count: {State.count}"

def reset():
    State.count = 0
    count_label.text = f"Count: 0"



#----------------------Layout----------------------------
ui.label("Welcome to nicegui!").style("color: green; font-size: 40px")

# Create an overall row for everything
with ui.row().classes("w-full"):
    with ui.column().classes("flex-1"):
        # Create a card for the greeting
        with ui.card().classes("h-65 w-full"):
            input_field = ui.input("Enter your name")
            ui.button("Greet Me", color = "green", on_click = greet)

    with ui.column().classes("flex-1"):
        # Create a card for the counter
        with ui.card().classes("h-65 w-full"):
            count_label = ui.label("Count: 0").classes("text-lg")
            # Create a row for the buttons
            with ui.row().classes():
                ui.button("Add one", color = "green", on_click = add_one)
                ui.button("Reset Count", color = "red", on_click = reset)
            # creating a label slider
            label_slider = ui.label("Step: 5").classes("text-lg")
            slider = ui.slider(min=1, max=10, value=5)
            slider.on("update:model-value", lambda: label_slider.set_text(f"Step: {slider.value}"))
    
n1 = ui.number("Number 1", value = 0).classes("w-24")
ui.label("+").classes("text-lg")
n2 = ui.number("Number 2", value = 0).classes("w-24")
ui.label("=").classes("text-lg")
result = ui.label("0").classes("text-lg")

#TODO Make the above work so that it works as an addition
#TODO Make the above look good as well when spare time allows
#TODO Extra Challenge: Allow the user to pick the operator to use

ui.switch("Dark mode", on_change= lambda x: ui.dark_mode().enable() if x.value else ui.dark_mode().disable()) 



ui.run(title="Intro to nicegui")