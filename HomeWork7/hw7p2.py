from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle: Completed
EMOJIS = ["\U0001f600", "\U0001F606", "\U0001F601", "\U0001F60E", "\U0001F610", "\U0001F631", "\U0001F634", "\U0001F609"]  # ← Your task
EMOJIS = list(EMOJIS + EMOJIS) #duplicates the emojis list
shuffle (EMOJIS) #shuffles the emojis list
print(EMOJIS) # debug code

buttons = []
print(buttons) # debug code

opened = []    # indices of currently flipped cards
matched = []   # indices of solved cards

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    pass

# TODO 3: Write click handler
def handle_click(idx):
    pass

# Build 4x4 grid
with ui.grid(columns=4).classes("h-200"):
    # TODO 4: Create 16 buttons
    button1 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button2 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button3 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button4 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button5 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button6 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button7 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button8 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button9 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button10 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button11 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button12 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button13 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button14 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button15 = ui.button(on_click = handle_click).classes("h-65, w-65")
    button16 = ui.button(on_click = handle_click).classes("h-65, w-65")

    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button15]

ui.run(title='Memory Game')