#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.7

from guizero import App, Box, Combo, PushButton, Slider, Text, TextBox

app = App(title="Pygzedit")

# function for reading files
def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()
    change_font()
    update_statusbar()

# function for writing files
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)
    lbl_saved.value = "Saved"

def update_statusbar():
    txt_num_chars.value = len(editor.value)
    lbl_saved.value = ""

def change_font():
    editor.font = cmb_font.value
    editor.text_size = sld_fontsize.value

# create a box to house the controls, we want the box to span the entire width of the app
file_controls = Box(app, align="top", width="fill")
toolbar = Box(app, align="top", width="fill")
statusbar = Box(app, align="bottom", width="fill")

cmb_font = Combo(toolbar, align="left", options=["Arial", "Comic Sans MS", "Courier New", "Marker Felt", "Menlo", "Tahoma", "Times New Roman", "Verdana"], selected="Menlo", command=change_font)
sld_fontsize = Slider(toolbar, align="left", start=8, end=32, command=change_font)
sld_fontsize.value = 12

# create a TextBox for the file name
file_name = TextBox(file_controls, text="test.txt", width=50, align="left")

# create a save button which uses the save_file function
save_button = PushButton(file_controls, text="Save", command=save_file, align="right")

# create an open button which uses the open_file function
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

# create a TextBox which is not in the box and fills the rest of the GUI
editor = TextBox(app, multiline=True, scrollbar=True, width="fill", height="fill", command=update_statusbar)

lbl_num_chars = Text(statusbar, text="Chars:", color="#B2B2B2", align="left")
txt_num_chars = TextBox(statusbar, enabled=False, text="", align="left")
lbl_saved = Text(statusbar, text="", color="#B2B2B2", align="right")

app.display()
