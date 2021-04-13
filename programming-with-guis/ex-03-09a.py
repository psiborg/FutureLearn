#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9a

from time import sleep

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        sleep(1)

countdown(10)
