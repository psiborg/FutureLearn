#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9 (alternate)

from guizero import App, PushButton, Text

def alternate():
    if button.bg == "white":
        button.bg = "black"
    else:
        button.bg = "white"
    return

app = App("alternate")

button = PushButton(app, text="Click me")
button.bg = "white"
button.repeat(100, alternate)

app.display()
