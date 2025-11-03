from nicegui import ui

ui.label("Welcome to nicegui!").style("color: green; font-size: 40px")



input_field = ui.input("Enter your name")

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}"
    ui.notify(msg)


ui.button("Greet Me", color = "green", on_click = greet)

#Create a counter
class State:
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"

def reset():
    State.count = 0
    count_label.text = f"Count: 0"

ui.button("Add one", color = "green", on_click = add_one)

ui.button("Reset Count", color = "red", on_click = reset)

ui.run(title="Intro to nicegui")