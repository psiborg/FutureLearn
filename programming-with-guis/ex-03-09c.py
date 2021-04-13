#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9c

from guizero import App, Text

def increase():
    text.text_size = int(text.text_size) + 1

app = App("textsize")

text = Text(app, text="bigger")
text.repeat(500, increase)

app.display()
