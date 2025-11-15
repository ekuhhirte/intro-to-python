from nicegui import ui
from random import shuffle
import time

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
    print(f"RESETTING, {i}, {j} ")
    i.text = ""
    j.text = ""

# TODO 3: Write click handler
def handle_click(button, id):
    global opened
    global matched
    if len(opened) >= 2:
        opened = []
    
    button.text = f"{EMOJIS[id-1]}"
    opened.append(id)

    if len(opened) > 1: #if you have two flipped cards
        if EMOJIS[opened[0]-1] == EMOJIS[opened[1]-1]: #checks if the cards are the same
            print(f"MATCHED, {EMOJIS[opened[0]-1]}, {EMOJIS[opened[1]-1]}")
            matched.append(opened[0])
            matched.append(opened[1])
            if len(matched) == 16:
                pass
        else:
            #print(f"RESET: {opened}") #debug code commented off
            ui.timer(0.5, lambda: reset_pair(buttons[opened[0]-1], buttons[opened[1]-1]), once = True)
             #pauses program execution for 0.5 second

# Build 4x4 grid
with ui.grid(columns=4).classes("h-200"):
    # TODO 4: Create 16 buttons
    button1 = ui.button(on_click = lambda: handle_click(button1, 1)).classes("h-65, w-65")
    button2 = ui.button(on_click = lambda: handle_click(button2, 2)).classes("h-65, w-65")
    button3 = ui.button(on_click = lambda: handle_click(button3, 3)).classes("h-65, w-65")
    button4 = ui.button(on_click = lambda: handle_click(button4, 4)).classes("h-65, w-65")
    button5 = ui.button(on_click = lambda: handle_click(button5, 5)).classes("h-65, w-65")
    button6 = ui.button(on_click = lambda: handle_click(button6, 6)).classes("h-65, w-65")
    button7 = ui.button(on_click = lambda: handle_click(button7, 7)).classes("h-65, w-65")
    button8 = ui.button(on_click = lambda: handle_click(button8, 8)).classes("h-65, w-65")
    button9 = ui.button(on_click = lambda: handle_click(button9, 9)).classes("h-65, w-65")
    button10 = ui.button(on_click = lambda: handle_click(button10, 10)).classes("h-65, w-65")
    button11 = ui.button(on_click = lambda: handle_click(button11, 11)).classes("h-65, w-65")
    button12 = ui.button(on_click = lambda: handle_click(button12, 12)).classes("h-65, w-65")
    button13 = ui.button(on_click = lambda: handle_click(button13, 13)).classes("h-65, w-65")
    button14 = ui.button(on_click = lambda: handle_click(button14, 14)).classes("h-65, w-65")
    button15 = ui.button(on_click = lambda: handle_click(button15, 15)).classes("h-65, w-65")
    button16 = ui.button(on_click = lambda: handle_click(button16, 16)).classes("h-65, w-65")

    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button15, button16]
    

ui.run(title='Memory Game')