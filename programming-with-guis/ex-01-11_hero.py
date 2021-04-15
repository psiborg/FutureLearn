#!/usr/bin/env python3
# programming-with-guis
# Ex. 1.11

from guizero import App, ButtonGroup, CheckBox, Combo, ListBox, Picture, PushButton, Slider, Text, TextBox
import textwrap

char_class = {
    1: {
        "name": "Barbarian",
        "desc": "A fierce warrior of primitive background who can enter a battle rage",
        "file": "class_barbarian.gif"
    },
    2: {
        "name": "Bard",
        "desc": "An inspiring magician whose power echoes the music of creation",
        "file": "class_bard.gif"
    },
    3: {
        "name": "Cleric",
        "desc": "A priestly champion who wields divine magic in service of a higher power",
        "file": "class_cleric.gif"
    },
    4: {
        "name": "Druid",
        "desc": "A priest of the old faith, wielding the powers of nature and adopting animal forms",
        "file": "class_druid.gif"
    },
    5: {
        "name": "Fighter",
        "desc": "A master of martial combat, skilled with a variety of weapons and armor",
        "file": "class_fighter.gif"
    },
    6: {
        "name": "Monk",
        "desc": "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritial perfection",
        "file": "class_monk.gif"
    },
    7: {
        "name": "Paladin",
        "desc": "A holy warrior bound to a sacret oath",
        "file": "class_paladin.gif"
    },
    8: {
        "name": "Ranger",
        "desc": "A warrior who combats threats on the edges of civilization",
        "file": "class_ranger.gif"
    },
    9: {
        "name": "Rogue",
        "desc": "A scoundrel who uses stealth and trickery to overcome obstacles and enemies",
        "file": "class_rogue.gif"
    },
    10: {
        "name": "Sorcerer",
        "desc": "A spellcaster who draws on inherent magic from a gift of bloodline",
        "file": "class_sorcerer.gif"
    },
    11: {
        "name": "Warlock",
        "desc": "A wielder of magic that is derived from a bargain with an extraplanar entity",
        "file": "class_warlock.gif"
    },
    12: {
        "name": "Wizard",
        "desc": "A scholarly magic-user capable of manipulating the structures of reality",
        "file": "class_wizard.gif"
    }
}

app = App(title="Hero-o-matic v2.0", width=640, height=680, layout="grid", bg="#c0c0c0")

# Function definitions for your events go here

def slider_class(sld_val):
    num = int(sld_val)
    pic_class.value = "./assets/" + char_class[num]['file']
    txt_class.value = char_class[num]['name']

    lines = ''
    for line in (textwrap.wrap(char_class[num]['desc'], width=30)):
        lines += line + "\n"
    txt_class_desc.value = lines

def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    char = txt_class.value
    hero = adjective + " " + colour + " " + animal + " " + char
    lbl_line.value = "You are..."
    lbl_hero.value = "The " + hero
    lbl_hero.text_color = colour

def villainize():
    if chk_villain.value == 1:
        app.bg = "#666666"
    else:
        app.bg = "#c0c0c0"

# Your GUI widgets go here

lbl_class = Text(app, text="Class:", grid=[0,0])
sld_class = Slider(app, start="1", end="12", command=slider_class, grid=[0,1])
pic_class = Picture(app, image="./assets/class_barbarian.gif", grid=[0,2])

txt_class = Text(app, width="fill", grid=[1,0])
txt_class_desc = Text(app, align="top", height="fill", grid=[1,1,1,2])

lbl_adjective = Text(app, text="Adjective:", grid=[0,3])
bgp_adjective = ButtonGroup(app, options=["Amazing", "Galactic", "Incredible", "Magnificent", "Mighty", "Valiant"], align="top", selected="Magnificent", grid=[0,4])

lbl_colour = Text(app, text="Colour:", grid=[1,3])
txt_colour = ListBox(app, items=["Black", "White", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"], align="top", selected="Black", grid=[1,4])

lbl_animal = Text(app, text="Animal", grid=[2,3])
cmb_animal = Combo(app, options=["Bear", "Crow", "Deer", "Dolphin", "Eagle", "Hawk", "Horse", "Lion", "Owl", "Panda", "Panther", "Shark", "Snake", "Tiger", "Wolf"], align="top", selected="Panther", grid=[2,4])

chk_villain = CheckBox(app, text="Villain", command=villainize, grid=[0,5])

btn_generate = PushButton(app, text="Generate", command=make_hero_name, grid=[0,6,3,1])

lbl_line = Text(app, text="", grid=[0,7,3,1])
lbl_hero = Text(app, text="", size="20", grid=[0,8,3,1])

# Set up event triggers here

# Show the GUI on the screen, start listening to events

app.display()
