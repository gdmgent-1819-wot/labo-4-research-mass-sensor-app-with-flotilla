# Piano with flotilla touch and rainbow

import colorsys
import sys
import time
import pygame       
import flotilla

try:
    dock = flotilla.Client(
       requires={
            'one': flotilla.Touch,
            'two': flotilla.Rainbow
        })
except KeyboardInterrupt:
    sys.exit(1)

while not dock.ready:
    pass

touch = dock.first(flotilla.Touch)
rainbow = dock.first(flotilla.Rainbow)
hue = 0
lights_on = True

def Sound_piano(nameSound):
    pygame.mixer.init()
    pygame.mixer.music.load(nameSound)
    pygame.mixer.music.play()

try:
    while True:
        if touch.one:
            hue += 60
            hue %= 360
            nameSound = "203458__tesabob2001__a3.mp3";
            Sound_piano(nameSound)
        if touch.two:
            hue += 60
            hue %= 360
            nameSound = "203459__tesabob2001__a-5.mp3";
            Sound_piano(nameSound)
        if touch.three:
            hue += 60
            hue %= 360
            nameSound = "203478__tesabob2001__c4-middle-c.mp3";
            Sound_piano(nameSound)
        if touch.four:
            hue += 60
            hue %= 360
            nameSound = "203479__tesabob2001__c3.mp3";
            Sound_piano(nameSound)
        r, g, b = 0, 0, 0
        if lights_on:
            r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]
        rainbow.set_all(r, g, b).update()
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopping")
    dock.stop()
