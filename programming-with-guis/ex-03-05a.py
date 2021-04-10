#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.5a

from guizero import App, Text, Box

app = App(layout="auto")

box = Box(app, layout="grid", width="fill", height="fill")

red = Text(box, bg="red", grid=[0,0], width=20)
blue = Text(box, bg="blue", grid=[0,1], width="fill")
green = Text(box, bg="green", grid=[1,0])
yellow = Text(box, bg="yellow", grid=[1,1])

app.display()
