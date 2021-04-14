#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.13

import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text, Window, warn

def load_emojis():
    emojis_dir = "./assets/emojis"
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)
    return emojis

def match_emoji(matched):
    global in_a_row
    if matched:
        in_a_row += 1
        result.value = "Correct"
        result.text_color = "green"
        score.value = int(score.value) + 1
        if in_a_row == 3:
            # add a bonus point
            #score.value = int(score.value) + 1
            #app.info("info", "Bonus points for 3 in a row!")

            # add extra time
            extra_time = randint(1,10)
            timer.value = int(timer.value) + extra_time
            result.value = "Extra " + str(extra_time) + " secs for 3 in a row!"
            result.text_color = "blue"
            in_a_row = 0
    else:
        result.value = "Incorrect"
        result.text_color = "red"
        score.value = int(score.value) - 1
        if in_a_row > 0:
            in_a_row -= 1

    setup_round()

def setup_round():
    rounds.value = int(rounds.value) + 1

    emojis = load_emojis()

    for picture in pictures:
        picture.image = emojis.pop()

    for button in buttons:
        button.image = emojis.pop()
        # set the command to be called and pass False, as these emoji wont be the matching ones
        button.update_command(match_emoji, [False])

    # choose a new emoji
    matched_emoji = emojis.pop()

    # select a number at random
    random_picture = randint(0,8)

    # change the image feature of the Picture with this index in the list of pictures to the new emoji
    pictures[random_picture].image = matched_emoji

    random_button = randint(0,8)
    print(random_button)

    # change the image feature of the PushButton with this index in the list of buttons to the new emoji
    buttons[random_button].image = matched_emoji

    # set the command to be called and pass True, as this is the matching emoji
    buttons[random_button].update_command(match_emoji, [True])

def reset():
    in_a_row = 0
    result.value = ""
    score.value = "0"
    setup_round()
    timer.value = "20"
    timer.repeat(1000, counter)
    return

def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(counter)
        result.value = "Game over!"
        result.text_color = "black"

        prompt = app.yesno("Times up!", "Do you want to play again?")
        if prompt == True:
            reset()

def start_1player():
    player1_name = app.question("Player 1", "Player 1 Name?")
    if player1_name is not None:
        reset()
    return

def start_2players():
    player2_name = app.question("Player 2", "Name?")
    if player2_name is not None:
        reset()
    return

def show_hiscores():
    global hi_scores

    high_scores = "High Scores\n"
    for x in hi_scores:
        print(x)
        high_scores += x["name"] + "\t" + x["score"] + "\n"

    wnd_hiscores.show(wait=True)
    return

def show_help():
    wnd_help.show(wait=True)
    return

# setup the app
app = App("emoji match", layout="auto", width=640, height=480)

wnd_hiscores = Window(app, title="High Scores", visible=False)
wnd_help = Window(app, title="Help", visible=False)

scoreboard = Box(app, align="top", width="fill", layout="grid")
scoreboard.bg = "#C0C0C0"

rounds_lbl = Text(scoreboard, text="Round: ", size=12, grid=[0,0])
spacer1 = Text(scoreboard, text=" ", width=40, grid=[1,0])
score_lbl = Text(scoreboard, text="Score: ", size=12, grid=[2,0])
spacer2 = Text(scoreboard, text=" ", width=40, grid=[3,0])
timer_lbl = Text(scoreboard, text="Timer: ", size=12, grid=[4,0])

rounds = Text(scoreboard, text="0", size=20, grid=[0,1])
score = Text(scoreboard, text="0", size=20, grid=[2,1])
timer = Text(scoreboard, text="0", size=20, grid=[4,1])

game_box = Box(app, align="top", layout="grid")
pictures_box = Box(game_box, layout="grid", grid=[0,2])
buttons_box = Box(game_box, layout="grid", grid=[1,2])
result = Text(game_box, size=24, grid=[0,3,2,1])

controls_box = Box(app, align="top", layout="grid")
btn_player1 = PushButton(controls_box, text="1 Player", image="./assets/btn_player1.gif", grid=[0,0], command=start_1player)
btn_player2 = PushButton(controls_box, text="2 Players", image="./assets/btn_player2.gif", grid=[1,0], command=start_2players)
btn_hiscores = PushButton(controls_box, text="High Scores", image="./assets/btn_hiscores.gif", grid=[2,0], command=show_hiscores)
btn_help = PushButton(controls_box, text="Help", image="./assets/btn_help.gif", grid=[3,0], command=show_help)

in_a_row = 0

hi_scores = [{
    "name": "Fred",
    "score": "10"
}, {
    "name": "Barney",
    "score": "9"
}]

buttons = []
pictures = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        
        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

app.display()
