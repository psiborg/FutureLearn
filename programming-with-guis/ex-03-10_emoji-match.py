#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.10

import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text, warn

# set the path to the emoji folder on your computer
def load_emojis():
    emojis_dir = "./assets/emojis"
    # create a list of the locations of the emoji images
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    # shuffle the emojis
    shuffle(emojis)
    return emojis

def match_emoji(matched):
    if matched:
        result.value = "correct"
    else:
        result.value = "incorrect"
        
    setup_round()

def setup_round():
    rounds.value = int(rounds.value) + 1

    emojis = load_emojis()
    #print(len(emojis))
    # for each picture and button in the list assign an emoji to its image feature
    for picture in pictures:
        # make the picture a random emoji
        picture.image = emojis.pop()

    for button in buttons:
        # make the image feature of the PushButton a random emoji
        button.image = emojis.pop()
        # set the command to be called and pass False, as these emoji wont be the matching ones
        button.update_command(match_emoji, [False])

    # choose a new emoji
    matched_emoji = emojis.pop()
    #print(len(emojis))

    # select a number at random
    random_picture = randint(0,8)
    # change the image feature of the Picture with this index in the list of pictures to the new emoji
    pictures[random_picture].image = matched_emoji

    random_button = randint(0,8)
    # change the image feature of the PushButton with this index in the list of buttons to the new emoji
    buttons[random_button].image = matched_emoji
    # set the command to be called and pass True, as this is the matching emoji
    buttons[random_button].update_command(match_emoji, [True])

    print(random_picture, random_button)

def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(counter)
        # reset the timer
        result.value = "Game over!"
        #warn("Time Out", "you've run out of time")
        prompt = app.yesno("Times up!", "Do you want to play again?")
        if prompt == True:
            # reset timer
            timer.value = "20"
            # reset result
            result.value = ""
            # start new round
            setup_round()
            #restart timer
            timer.repeat(1000, counter)

# setup the app
app = App("emoji match", width=640, height=480)

# create a box to house the grids
game_box = Box(app, layout="grid")

rounds_lbl = Text(game_box, text="Rounds: ", size=14, grid=[0,0])
timer_lbl = Text(game_box, text="Timer: ", size=14, grid=[1,0])

rounds = Text(game_box, text="0", size=16, grid=[0,1])
timer = Text(game_box, text="Get ready!", size=16, grid=[1,1])

# create a box to house the pictures
pictures_box = Box(game_box, layout="grid", grid=[0,2])

# create a box to house the buttons
buttons_box = Box(game_box, layout="grid", grid=[1,2])

result = Text(game_box, size=20, grid=[0,3,2,1])

# create the an empty lists to add the buttons and pictures to
buttons = []
pictures = []
# create 9 PushButtons with a different grid coordinate and add to the list
for x in range(0,3):
    for y in range(0,3):
        # put the pictures and buttons into the lists
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        
        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

setup_round()

# start the timer
timer.value = 20
timer.repeat(1000, counter)

app.display()
