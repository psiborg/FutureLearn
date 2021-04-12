#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.6b

import os
from random import shuffle
from guizero import App, Box, Picture

# set the path to the emoji folder on your computer
emojis_dir = "./assets/emojis"
# create a list of the locations of the emoji images
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
# shuffle the emojis
shuffle(emojis)

app = App("emoji match")
# create a box to house the grid
pictures_box = Box(app, layout="grid")

# create an empty list to which pictures will be added
pictures = []
for x in range(0,3):
    for y in range(0,3):
        # put the pictures into the list
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)

# for each picture in the list
for picture in pictures:
    # make the picture a random emoji
    picture.image = emojis.pop()

app.display()
