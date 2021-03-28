#!/usr/bin/env python3
# programming-with-guis
# Ex. 1.6b

# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_check_passwords():
    if txt_password1.value == txt_password2.value:
        info("Success", "Match!")
    else:
        info("Error", "Please try again")

# Your GUI widgets go here
lbl_password1 = Text(app, text="Password:")
txt_password1 = TextBox(app, hide_text=True)

lbl_password2 = Text(app, text="Confirm Password:")
txt_password2 = TextBox(app, hide_text=True)

btn_check = PushButton(app, command=btn_check_passwords, text="Check")

# Show the GUI on the screen
app.display()
