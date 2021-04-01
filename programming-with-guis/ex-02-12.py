#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.12

from guizero import App, Box, CheckBox, Combo, MenuBar, PushButton, Slider, Text, TextBox

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

def toggle_statusbar():
    if statusbar.visible == False:
        statusbar.show()
    else:
        statusbar.hide()

def toggle_toolbar():
    if toolbar.visible == False:
        toolbar.show()
    else:
        toolbar.hide()

def toggle_theme():
    print(editor.bg, editor.text_color)
    if editor.bg == "systemWindowBody" or editor.bg == "white":
        editor.bg = "black"
        editor.text_color = "white"
    else:
        editor.bg = "white"
        editor.text_color = "black"

# A new function that closes the app
def exit_app():
    if save_button.visible == True:
        if statusbar.visible == False:
            statusbar.show()
        lbl_warning.value = "Please save your file before exiting"
    else:
        app.destroy()

app = App(title="Pygzedit")

# The new MenuBar
menubar = MenuBar(app,
    toplevel = ["File", "View"],
    options = [[
        ["Open", open_file],
        ["Save", save_file],
        ["Exit", exit_app]
    ], [
        ["Dark/Light Theme", toggle_theme],
        ["Toolbar", toggle_toolbar],
        ["Statusbar", toggle_statusbar]
    ]]
)

file_controls = Box(app, align="top", width="fill", border=True)
toolbar = Box(app, align="top", width="fill", visible=False)
statusbar = Box(app, align="bottom", width="fill", visible=False)

cmb_font = Combo(toolbar, align="left", enabled=False, options=["Arial", "Comic Sans MS", "Courier New", "Marker Felt", "Menlo", "Tahoma", "Times New Roman", "Verdana"], selected="Menlo", command=change_font)
sld_fontsize = Slider(toolbar, align="left", enabled=False, start=8, end=32, command=change_font)
sld_fontsize.value = 12
cmb_colour = Combo(toolbar, align="left", enabled=False, options=["black", "red", "dark green", "blue"], selected="black", command=change_font)

file_name = TextBox(file_controls, text="test.txt", width=50, align="left")

save_button = PushButton(file_controls, text="Save", command=save_file, align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

editor = TextBox(app, multiline=True, height="fill", width="fill", command=update_statusbar)

lbl_num_chars = Text(statusbar, text="Chars:", color="#B2B2B2", align="left")
txt_num_chars = TextBox(statusbar, enabled=False, text="", align="left")
lbl_saved = Text(statusbar, text="", color="#B2B2B2", align="right")
lbl_warning = Text(statusbar, text="", bg="#FF0000", color="#FFFFFF", align="right")

app.display()
