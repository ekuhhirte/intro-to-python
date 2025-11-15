from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle: Completed
EMOJIS = ["\U0001f600", "\U0001F606", "\U0001F601", "\U0001F60E", "\U0001F610", "\U0001F631", "\U0001F634", "\U0001F609"]  # ← Your task
EMOJIS = list(EMOJIS + EMOJIS) #duplicates the emojis list
shuffle (EMOJIS) #shuffles the emojis list
print(EMOJIS)

buttons = []
opened = []    # indices of currently flipped cards
matched = []   # indices of solved cards

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    pass

# TODO 3: Write click handler
def handle_click(idx):
    pass

# Build 4x4 grid
with ui.grid(columns=4):
    # TODO 4: Create 16 buttons
    pass

#ui.run(title='Memory Game')