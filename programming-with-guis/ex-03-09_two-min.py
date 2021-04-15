#!/usr/bin/env python3
# programming-with-guis
# Ex. 3.9 (two minute timer)

from time import sleep

def convert(sec):
    ss = sec % (24 * 3600)
    hh = ss // 3600
    ss %= 3600
    mm = ss // 60
    ss %= 60
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)

def countdown(t):
    while True:
        if t > 0:
            hhmmss = convert(t)
            print(hhmmss)
            t -= 1
            sleep(1)
        else:
            print("Game over!")
            break

countdown(120)
