#!/usr/bin/env python3
# programming-with-guis
# Ex. 1.5

from guizero import App, Text
app = App(title = "My App")

line1 = Text(app, text = "Heading")
line2 = Text(app, text = "Subheading")
line3 = Text(app, text = "The quick brown fox jumps over the lazy dog.")

line1.font = "Times New Roman"
line1.text_color = "red"
line1.text_size = 40

line2.bg = "green"

app.display()
