#!/usr/bin/env python3
# programming-with-guis
# Ex. 2.4

# guizero - Hero name generator
from guizero import App, Box, ButtonGroup, Combo, ListBox, PushButton, Slider, Text, TextBox
app = App(title="Hero-o-matic", bg="#CCCCCC")

# https://www.looper.com/101942/powerful-avengers-mcu-ranked/
levels = {
    "1": "Spider-Man",
    "2": "Captain America",
    "3": "Iron Man",
    "4": "Black Panther",
    "5": "Scarlet Witch",
    "6": "The Vision",
    "7": "Doctor Strange",
    "8": "Thor",
    "9": "The Hulk",
    "10": "Captain Marvel"
}

bg_colours = {
    "Black": "#000000", 
    "White": "#FFFFFF", 
    "Red": "#990000", 
    "Yellow": "#999900", 
    "Green": "#009900", 
    "Cyan": "#009999", 
    "Blue": "#000099", 
    "Magenta": "#990099"
}

fg_colours = {
    "Black": "#FFFFFF", 
    "White": "#000000", 
    "Red": "#FFFFFF", 
    "Yellow": "#000000", 
    "Green": "#FFFFFF", 
    "Cyan": "#000000", 
    "Blue": "#FFFFFF", 
    "Magenta": "#000000"
}

# Function definitions for your events go here

def change_colour(val):
    box_colour.bg = bg_colours[val]
    box_colour.text_color = fg_colours[val]

def slider_changed(slider_value):
    txt_strength.value = levels[slider_value]

def make_hero_name():
    adjective = cmb_adjective.value
    colour = lst_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.text_size = 16
    lbl_output.text_color = bg_colours[lst_colour.value]
    lbl_output.value = "The " + hero + " (Strength=" + levels[str(sld_strength.value)] + ")"

# Your GUI widgets go here

box_adjective = Box(app, border=0)
lbl_adjective = Text(box_adjective, text="Adjective:")
cmb_adjective = Combo(box_adjective, options=["Amazing", "Galactic", "Incredible", "Magnificent", "Mighty", "Valiant"], selected="Amazing")

box_colour = Box(app, border=0)
box_colour.bg = "#999999"
lbl_colour = Text(box_colour, text="Colour:")
lst_colour = ListBox(box_colour, items=["Black", "White", "Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"], align="top", selected="Black", command=change_colour)

box_animal = Box(app, border=0)
lbl_animal = Text(box_animal, text="Animal:")
cmb_animal = Combo(box_animal, options=["Bear", "Crow", "Deer", "Dolphin", "Eagle", "Hawk", "Horse", "Lion", "Owl", "Panda", "Panther", "Shark", "Snake", "Tiger", "Wolf"], selected="Panther", width=20)

box_strength = Box(app, border=0)
lbl_strength = Text(box_strength, text="Strength level:")
sld_strength = Slider(box_strength, start="1", end="10", command=slider_changed)
txt_strength = Text(box_strength)

box_make_name = Box(app, border=0)
btn_make_name = PushButton(box_make_name, text="Generate", command=make_hero_name)

box_output = Box(app, border=1)
#box_output.bg = "#999999"
lbl_output = Text(box_output, text="Your hero name will appear here")

# Set up event triggers here

# Show the GUI on the screen, start listening to events

app.display()
