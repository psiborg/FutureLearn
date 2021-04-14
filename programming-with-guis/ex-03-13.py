#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.13

import os
from random import shuffle, randint
from guizero import App, Box, ListBox, Picture, PushButton, Text, Window, warn

def load_emojis():
    emojis_dir = "./assets/emojis"
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
    shuffle(emojis)
    return emojis

def match_emoji(matched):
    global in_a_row, player_num
    if matched:
        in_a_row += 1
        result.value = "Correct"
        result.text_color = "green"
        players[player_num]["score"].value = int(players[player_num]["score"].value) + 1
        if in_a_row == 3:
            # add a bonus point
            #players[player_num]["score"].value = int(players[player_num]["score"].value) + 1
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
        players[player_num]["score"].value = int(players[player_num]["score"].value) - 1
        if in_a_row > 0:
            in_a_row -= 1
    setup_round()

def setup_round():
    players[player_num]["round"].value = int(players[player_num]["round"].value) + 1

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
    global player_num
    in_a_row = 0
    result.value = ""
    players[player_num]["round"].value = "0"
    players[player_num]["score"].value = "0"
    setup_round()
    timer.value = "20"
    timer.repeat(1000, counter)
    return

def counter():
    global player_num

    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(counter)

        # add score to high scores
        hi_scores.append(tuple((players[player_num]["label"].value, int(players[player_num]["score"].value))))

        result.value = "Game over!"
        result.text_color = "black"

        prompt = app.yesno("Times up!", "Do you want to play again?")
        if prompt == True:
            reset()

def start_1player():
    global player_num
    player_num = "1"
    player_name = app.question("Player 1", "Enter your name")
    if player_name is not None:
        players[player_num]["label"].value = player_name
        reset()
    return

def start_2players():
    global player_num
    player_num = "2"
    player_name = app.question("Player 2", "Enter your name")
    if player_name is not None:
        players[player_num]["label"].value = player_name
        reset()
    return

# sort list of tuples by second element
# https://www.afternerd.com/blog/python-sort-list/#sort-tuples-second-element
def sort_hiscores(t):
    return t[1]

def show_hiscores():
    global hi_scores

    hi_title = Text(wnd_hiscores, align="top", text="Top Players", size=18)
    hi_box = Box(wnd_hiscores, align="top", layout="grid")
    hi_box.bg = "#CCCCCC"
    scores = []

    hi_scores.sort(reverse=True, key=sort_hiscores)
    print(hi_scores)

    for x in range(0, len(hi_scores)):
        hi_line = Text(hi_box, text=str(x+1)+". ", align="left", grid=[0,x])
        scores.append(hi_line)
        for y in range(0, len(hi_scores[x])):
            #print(x,y,hi_scores[x][y])
            hi_line = Text(hi_box, text=hi_scores[x][y], align="left", grid=[y+1,x])
            scores.append(hi_line)

    wnd_hiscores.show(wait=True) # modal window
    return

def show_help():
    wnd_help.show(wait=True) # modal window
    return

def clean_hiscores():
    #(wnd_hiscores.children)
    wnd_hiscores.hide()
    return

# setup the app
app = App("Emoji Match", layout="auto", width=640, height=480)

wnd_hiscores = Window(app, title="High Scores", visible=False)
wnd_hiscores.when_closed = clean_hiscores

wnd_help = Window(app, title="Help", visible=False)

scoreboard = Box(app, align="top", width="fill", layout="grid")
scoreboard.bg = "#C0C0C0"

players = {"1": {}, "2": {}}

players["1"]["label"] = Text(scoreboard, text="Player 1:", size=12, grid=[0,0,2,1])
spacer1 = Text(scoreboard, text=" ", width=35, grid=[2,0])
timer_lbl = Text(scoreboard, text="Timer: ", size=12, grid=[3,0])
spacer2 = Text(scoreboard, text=" ", width=35, grid=[4,0])
players["2"]["label"] = Text(scoreboard, text="Player 2:", size=12, grid=[5,0,2,1])

players["1"]["score_label"] = Text(scoreboard, text="Score", size=10, grid=[0,1])
players["1"]["round_label"] = Text(scoreboard, text="Round", size=10, grid=[1,1])
timer = Text(scoreboard, text="0", size=20, grid=[3,1])
players["2"]["score_label"] = Text(scoreboard, text="Score", size=10, grid=[5,1])
players["2"]["round_label"] = Text(scoreboard, text="Round", size=10, grid=[6,1])

players["1"]["score"] = Text(scoreboard, text="0", size=20, grid=[0,2])
players["1"]["round"] = Text(scoreboard, text="0", size=20, grid=[1,2])
players["2"]["score"] = Text(scoreboard, text="0", size=20, grid=[5,2])
players["2"]["round"] = Text(scoreboard, text="0", size=20, grid=[6,2])

game_box = Box(app, align="top", layout="grid")
result = Text(game_box, text="Ready?", size=24, grid=[0,0,2,1])
pictures_box = Box(game_box, layout="grid", grid=[0,1])
buttons_box = Box(game_box, layout="grid", grid=[1,1])
instructions = Text(game_box, text="Choose an option:", size=10, grid=[0,2,2,1])

controls_box = Box(app, align="top", layout="grid")
btn_player1 = PushButton(controls_box, text="1 Player", image="./assets/btn_player1.gif", grid=[0,0], command=start_1player)
btn_player2 = PushButton(controls_box, text="2 Players", image="./assets/btn_player2.gif", grid=[1,0], command=start_2players)
btn_hiscores = PushButton(controls_box, text="High Scores", image="./assets/btn_hiscores.gif", grid=[2,0], command=show_hiscores)
btn_help = PushButton(controls_box, text="Help", image="./assets/btn_help.gif", grid=[3,0], command=show_help)

in_a_row = 0
player_num = ""

hi_scores = [
    ("Tony Stark", 9),
    ("Steve Rogers", 8),
    ("Natasha Romanoff", 10)
]

buttons = []
pictures = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        
        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

app.display()
