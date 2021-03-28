#!/usr/bin/env python3
# programming-with-guis
# Ex. 1.6a

# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_submit_clicked():
    info("Greetings", "Hello " + txt_name.value + ". I see you like " + txt_animal.value + ".")

def btn_cancel_clicked():
    info("Greetings", "Hello " + txt_name.value + ". So you're not sure if you like " + txt_animal.value + "?")

# Your GUI widgets go here
lbl_name = Text(app, text="Your name?")
txt_name = TextBox(app)

lbl_animal = Text(app, text="Favorite animal?")
txt_animal = TextBox(app)

btn_submit = PushButton(app, command=btn_submit_clicked, text="Submit")
btn_cancel = PushButton(app, command=btn_cancel_clicked, text="Cancel")

# Show the GUI on the screen
app.display()
