#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.9

from guizero import App, Box, Combo, PushButton, Slider, Text, TextBox

app = App(title="Pygzedit")

def enable_toolbar():
    if cmb_font.enabled == False:
        cmb_font.enable()
    if sld_fontsize.enabled == False:
        sld_fontsize.enable()
    if cmb_colour.enabled == False:
        cmb_colour.enable()

def enable_save():
    if save_button.visible == False:
        save_button.show()

def disable_save():
    if save_button.visible == True:
        save_button.hide()

# function for reading files
def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()
    update_statusbar()

# function for writing files
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)
    lbl_saved.value = "Saved"
    disable_save()

def update_statusbar():
    txt_num_chars.value = len(editor.value)
    lbl_saved.value = ""
    enable_toolbar()
    enable_save()

def change_font():
    editor.text_color = cmb_colour.value
    editor.font = cmb_font.value
    editor.text_size = sld_fontsize.value
    # resize the widget because if the text is made bigger, this might affect the size of the TextBox so guizero needs to know how to maintain the intended layout
    editor.resize(1, 1)
    editor.resize("fill", "fill")

# create a box to house the controls, we want the box to span the entire width of the app
file_controls = Box(app, align="top", width="fill")
toolbar = Box(app, align="top", width="fill")
statusbar = Box(app, align="bottom", width="fill")

cmb_font = Combo(toolbar, align="left", enabled=False, options=["Arial", "Comic Sans MS", "Courier New", "Marker Felt", "Menlo", "Tahoma", "Times New Roman", "Verdana"], selected="Menlo", command=change_font)
sld_fontsize = Slider(toolbar, align="left", enabled=False, start=8, end=32, command=change_font)
sld_fontsize.value = 12
cmb_colour = Combo(toolbar, align="left", enabled=False, options=["black", "red", "dark green", "blue"], selected="black", command=change_font)

# create a TextBox for the file name
file_name = TextBox(file_controls, text="test.txt", width=50, align="left")

# create a save button which uses the save_file function
save_button = PushButton(file_controls, text="Save", command=save_file, align="right", visible=False)

# create an open button which uses the open_file function
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

# create a TextBox which is not in the box and fills the rest of the GUI
editor = TextBox(app, multiline=True, scrollbar=True, width="fill", height="fill", command=update_statusbar)

lbl_num_chars = Text(statusbar, text="Chars:", color="#B2B2B2", align="left")
txt_num_chars = TextBox(statusbar, enabled=False, text="", align="left")
lbl_saved = Text(statusbar, text="", color="#B2B2B2", align="right")

app.display()
