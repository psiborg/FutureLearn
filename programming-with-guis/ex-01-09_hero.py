#!/usr/bin/env python3
# programming-with-guis
# Ex. 1.9

# guizero - Hero name generator
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, ListBox, Slider
app = App(title="Hero-o-matic")

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

# Function definitions for your events go here.
def slider_changed(slider_value):
    txt_strength.value = levels[slider_value]

def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are...\nThe " + hero + " (Strength=" + levels[str(sld_strength.value)] + ")"

# Your GUI widgets go here
message1 = Text(app, text="Choose an adjective")
bgp_adjective = ListBox(app, items=["Amazing", "Bonny", "Charming", "Delightful", "Gutsy", "Lionhearted", "Plucky", "Spunky", "Valiant"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Cat", "Dolphin", "Tiger", "Velociraptor", "Walrus"], selected="Aardvark", width=20)

message4 = Text(app, text="Strength level")
sld_strength = Slider(app, start="1", end="10", command=slider_changed)
txt_strength = TextBox(app)

btn_make_name = PushButton(app, text='Make me a hero', command=make_hero_name)

lbl_output = Text(app, text="A hero name will appear here")

# Set up event triggers here

# Show the GUI on the screen, start listening to events.
app.display()
