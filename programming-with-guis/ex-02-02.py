#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.2

from guizero import App, Box, ButtonGroup, PushButton, Text

app = App(title="Ex. 2.2", width=640, height=480, bg="#c0c0c0")

txt_heading = Text(app, text="Boxed In", size=16, color="blue")

box_top = Box(app, align="top", border=1, width=630, height=200)

box_nav = Box(box_top, align="left", border=1, width=242, height=150)
bgp_opts = ButtonGroup(box_nav, options=["Basic", "Intermediate", "Advanced"], selected="Basic")

box_main = Box(box_top, align="right", border=1, width=378, height=150)
txt_main = Text(box_main, text="The quick brown fox jumps over the lazy dog.")

box_bottom = Box(app, align="bottom", border=1, width=160, height=100)
btn_submit = PushButton(box_bottom, text="Submit", align="left")
btn_reset = PushButton(box_bottom, text="Reset", align="right")

app.display()
