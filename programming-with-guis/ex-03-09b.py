#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9b

# When you try to run this code, your code appears to have frozen 
# and the app is not working

from guizero import App, Text
from time import sleep

def countdown(t):
    while t > 0:
        text.value = int(text.value) - 1
        sleep(1)

app = App()
text = Text(app, text=10)
countdown(10)

# creates an infinite loop that waits for events
app.display()
