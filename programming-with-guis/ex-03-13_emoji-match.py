#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.13

import os, pickle
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
    pictures_box.visible = True
    buttons_box.visible = True

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

def reset_game():
    global player_num, in_a_row
    in_a_row = 0
    result.value = ""
    players[player_num]["round"].value = "0"
    players[player_num]["score"].value = "0"
    setup_round()
    timer.value = "20"
    timer.repeat(1000, counter)
    return

def counter():
    global hi_scores, player_num

    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(counter)

        # add score to high scores
        hi_scores.append(tuple((players[player_num]["label"].value, int(players[player_num]["score"].value))))
        print(hi_scores)
        save_hiscores()

        # check who won
        msg = "Game over!"
        if int(players["1"]["round"].value) > 1 and int(players["2"]["round"].value) > 1:
            print(players["1"]["score"].value, players["2"]["score"].value)
            if int(players["1"]["score"].value) > int(players["2"]["score"].value):
                msg = "Player 1 won!"
            elif int(players["2"]["score"].value) > int(players["1"]["score"].value):
                msg = "Player 2 won!"
            else:
                msg = "It's a draw"

        result.value = msg
        result.text_color = "black"

        app.info("Info", msg)

        # prompt = app.yesno(msg, "Do you want to play again?")
        # if prompt == True:
        #     reset_game()

def start_game(num):
    global player_num
    player_num = num
    player_name = app.question("Player " + num, "Enter your name")
    if player_name is not None:
        players[num]["label"].value = player_name
        if num == "1":
            spacer1.value = "<<<"
            spacer2.value = " "
        elif num == "2":
            spacer1.value = " "
            spacer2.value = ">>>"
        else:
            spacer1.value = " "
            spacer2.value = " "

        reset_game()
    return

def load_hiscores():
    if os.path.exists("hiscores.dat"):
        fh = open('hiscores.dat', 'rb')
        # deserialize data
        hi_scores = pickle.load(fh)
        fh.close()
    else:
        # populate with sample scores
        hi_scores = [
            ("Carol Danvers", 10),
            ("Bruce Banner", 9),
            ("Thor Odinson", 8),
            ("Stephen Strange", 7),
            ("Wanda Maximoff", 6),
            ("Tony Stark", 5),
            ("Steve Rogers", 4),
            ("Peter Parker", 3),
            ("Scott Lang", 2),
            ("Natasha Romanoff", 1)
        ]
    #print("load_hiscores:", hi_scores, type(hi_scores))
    return hi_scores

def save_hiscores():
    global hi_scores
    #print("save_hiscores:", hi_scores)
    fh = open('hiscores.dat', 'wb')
    # serialize data
    pickle.dump(hi_scores, fh)
    fh.close()
    return

# sort list of tuples by second element
# https://www.afternerd.com/blog/python-sort-list/#sort-tuples-second-element
def sort_hiscores(t):
    return t[1]

def show_hiscores():
    global hi_scores

    hi_title = Text(wnd_hiscores, align="top", text="Top Players", size=18)
    hi_box = Box(wnd_hiscores, align="top", layout="grid")
    #hi_box.bg = "#CCCCCC"
    scores = []

    hi_scores.sort(reverse=True, key=sort_hiscores)
    #print(hi_scores)

    for x in range(0, len(hi_scores)):
        if x < 20:
            hi_line = Text(hi_box, text=str(x+1)+". ", align="left", grid=[0,x])
            scores.append(hi_line)
            for y in range(0, len(hi_scores[x])):
                #print(x,y,hi_scores[x][y])
                hi_line = Text(hi_box, text=hi_scores[x][y], align="left", grid=[y+1,x])
                scores.append(hi_line)
        else:
            break

    wnd_hiscores.show(wait=True) # modal window
    return

def show_help():
    wnd_help.show(wait=True) # modal window
    return

# clear the contents since the high score list is appended each time the
# window is opened
def clear_hiscores_window():
    for child in wnd_hiscores.children:
        #print(child, type(child))
        if hasattr(child, 'children'):
            if child.children:
                for grandchild in child.children:
                    grandchild.destroy()
                child.destroy()

    for child in wnd_hiscores.children:
        child.destroy()

    wnd_hiscores.hide()
    return

def quit_app():
    confirm = app.yesno("Confirm", "Do you want to exit?")
    if confirm == True:
        app.destroy()

    app.display()
    return

#---[ Main ]------------------------------------------------------------------

app = App("Emoji Match", layout="auto", width=640, height=480)

in_a_row = 0
player_num = ""

# Set up High Score window

wnd_hiscores = Window(app, title="High Scores", bg="#DDDDDD", visible=False)
wnd_hiscores.when_closed = clear_hiscores_window

hi_scores = load_hiscores()

# Set up Help window

wnd_help = Window(app, title="Help", bg="#DDDDDD", visible=False)
help_box = Box(wnd_help, align="top", width="fill", layout="grid")

help_sec1_title = Text(help_box, text="How to play:", align="left", size=16, grid=[0,0])
help_sec1_line1 = Text(help_box, text="    ◉ Each player takes turns by clicking either the 'Player 1' or 'Player 2' buttons", align="left", grid=[0,1])

help_sec2_title = Text(help_box, text="Scoring:", align="left", size=16, grid=[0,2])
help_sec2_line1 = Text(help_box, text="    ◉ +1 pt for correct matches", align="left", grid=[0,3])
help_sec2_line2 = Text(help_box, text="    ◉ –1 pt for incorrect guesses", align="left", grid=[0,4])
help_sec2_line3 = Text(help_box, text="    ◉ For 3 matches in a row, extra time is added, randomly between 1-10 secs.", align="left", grid=[0,5])

# Set up scoreboard

scoreboard = Box(app, align="top", width="fill", layout="grid")
scoreboard.bg = "#C0C0C0"

players = {"1": {}, "2": {}}

players["1"]["label"] = Text(scoreboard, text="Player 1:", size=12, grid=[0,0,2,1])
spacer1 = Text(scoreboard, text=" ", color="#990000", size=20, width=20, grid=[2,0,1,3])
timer_lbl = Text(scoreboard, text="Timer: ", size=12, grid=[3,0])
spacer2 = Text(scoreboard, text=" ", color="#990000", size=20, width=20, grid=[4,0,1,3])
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

# Set up game grids

game_box = Box(app, align="top", layout="grid")
result = Text(game_box, text="Ready?", size=24, grid=[0,0,3,1])
pictures_box = Box(game_box, layout="grid", grid=[0,1], visible=False)
spacer3 = Text(game_box, text=" ", width=10, grid=[1,1])
buttons_box = Box(game_box, layout="grid", grid=[2,1], visible=False)
instructions = Text(game_box, text="Choose an option:", size=10, grid=[0,2,3,1])

buttons = []
pictures = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        
        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

# Set up player controls

controls_box = Box(app, align="top", layout="grid")
btn_player1 = PushButton(controls_box, text="1 Player", image="./assets/btn_player1.gif", grid=[0,0], command=start_game, args=["1"])
btn_player2 = PushButton(controls_box, text="2 Players", image="./assets/btn_player2.gif", grid=[1,0], command=start_game, args=["2"])
btn_hiscores = PushButton(controls_box, text="High Scores", image="./assets/btn_hiscores.gif", grid=[2,0], command=show_hiscores)
btn_help = PushButton(controls_box, text="Help", image="./assets/btn_help.gif", grid=[3,0], command=show_help)
btn_exit = PushButton(controls_box, text="Exit", image="./assets/btn_exit.gif", grid=[4,0], command=quit_app)

app.display()
