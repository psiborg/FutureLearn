#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.11

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
    global in_a_row
    if matched:
        in_a_row += 1
        result.value = "Correct"
        score.value = int(score.value) + 1
        if in_a_row == 3:
            # add a bonus point
            #score.value = int(score.value) + 1
            #app.info("info", "Bonus points for 3 in a row!")

            # add extra time
            extra_time = randint(1,10)
            timer.value = int(timer.value) + extra_time
            app.info("info", "Extra " + str(extra_time) + " secs for 3 in a row!")

            in_a_row = 0
    else:
        result.value = "Incorrect"
        score.value = int(score.value) - 1
        if in_a_row > 0:
            in_a_row -= 1

    print(in_a_row)
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

        prompt = app.yesno("Times up!", "Do you want to play again?")
        if prompt == True:
            # reset timer
            timer.value = "20"
            # reset result
            result.value = ""
            # reset score
            score.value = "0"
            # reset in-a-row
            in_a_row = 0
            # start new round
            setup_round()
            #restart timer
            timer.repeat(1000, counter)

# setup the app
app = App("emoji match", layout="auto", width=640, height=480)

scoreboard = Box(app, align="top", width="fill", layout="grid")
scoreboard.bg = "#C0C0C0"

rounds_lbl = Text(scoreboard, text="Round: ", size=12, grid=[0,0])
spacer1 = Text(scoreboard, text=" ", width=38, grid=[1,0])
score_lbl = Text(scoreboard, text="Score: ", size=12, grid=[2,0])
spacer2 = Text(scoreboard, text=" ", width=38, grid=[3,0])
timer_lbl = Text(scoreboard, text="Timer: ", size=12, grid=[4,0])

rounds = Text(scoreboard, text="0", size=20, grid=[0,1])
score = Text(scoreboard, text="0", size=20, grid=[2,1])
timer = Text(scoreboard, text="Get ready!", size=20, grid=[4,1])

game_box = Box(app, align="top", layout="grid")

pictures_box = Box(game_box, layout="grid", grid=[0,2])

buttons_box = Box(game_box, layout="grid", grid=[1,2])

result = Text(game_box, size=24, grid=[0,3,2,1])

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

in_a_row = 0

app.display()
