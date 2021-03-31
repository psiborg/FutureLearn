#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.6b

from guizero import App, Text

# this time we have not set the layout to auto as it is default
app = App(title="align")

# create a series of widgets each with a different alignment
top_text_1 = Text(app, text="top_text_1", align="top", bg="#330000", color="#FFFFFF", width="fill", height="fill")
top_text_2 = Text(app, text="top_text_2", align="top", bg="#990000", color="#FFFFFF")
top_text_3 = Text(app, text="top_text_3", align="top", bg="#FF0000", color="#FFFFFF")

bottom_text_1 = Text(app, text="bottom_text_1", align="bottom", bg="#003333", color="#FFFFFF", width="fill")
bottom_text_2 = Text(app, text="bottom_text_2", align="bottom", bg="#009999", color="#FFFFFF")
bottom_text_3 = Text(app, text="bottom_text_3", align="bottom", bg="#00FFFF", color="#000000")

left_text_1 = Text(app, text="left_text_1", align="left", bg="#003300", color="#FFFFFF")
left_text_2 = Text(app, text="left_text_2", align="left", bg="#009900", color="#FFFFFF", height=5)
left_text_3 = Text(app, text="left_text_3", align="left", bg="#00FF00", color="#000000", width="fill", height=10)

right_text_1 = Text(app, text="right_text_1", align="right", bg="#000033", color="#FFFFFF", height="fill")
right_text_2 = Text(app, text="right_text_2", align="right", bg="#000099", color="#FFFFFF")
right_text_3 = Text(app, text="right_text_3", align="right", bg="#0000FF", color="#FFFFFF")

app.display()
