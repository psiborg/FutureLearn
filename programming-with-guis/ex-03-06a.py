#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.6a

import os
from random import shuffle
# set the path to the emoji folder on your computer
emojis_dir = "./assets/emojis"
# create a list of the locations of the emoji images
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
# shuffle the emojis
shuffle(emojis)
print(emojis)