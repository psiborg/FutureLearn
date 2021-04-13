#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9 (game over)

from time import sleep

def countdown(t):
    while True:
        if t > 0:
            print(t)
            t -= 1
            sleep(1)
        else:
            print("Game over!")
            break

countdown(10)
