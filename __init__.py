import display
import buttons
import mch22
from machine import Pin
from neopixel import NeoPixel
import time


def reboot(pressed):
    if pressed:
        mch22.exit_python()


def infinite(pressed):
    if pressed:
        while True:
            CyberSeals()


def CyberSeals():
    loop(3)
    loop(2)
    loop(1)
    display.drawFill(0x000000)
    # Needs to be changed to match hatchery project name. Spaces are underscores.
    display.drawPng(0, 0, '/apps/python/cyberseals/logo01.png')
    display.flush()
    # set some colors for the pixels (RGB)
    np[0] = (255, 255, 0)
    np[1] = (255, 255, 0)
    np[2] = (255, 255, 0)
    np[3] = (255, 255, 0)
    np[4] = (255, 255, 0)
    np.write()
    time.sleep(10)


def loop(x):
    np[0] = (0, 0, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    for y in range(0, x, 1):
        np[y] = (255, 255, 0)
    display.drawFill(0x000000)
    # Needs to be changed to match hatchery project name. Spaces are underscores.
    display.drawPng(0, 0, '/apps/python/cyberseals/' + str(x) + '.png')
    display.flush()
    np.write()
    time.sleep(1)


buttons.attach(buttons.BTN_A, infinite)
buttons.attach(buttons.BTN_B, reboot)
display.drawFill(0x000000)
display.flush()
powerPin = Pin(19, Pin.OUT)
dataPin = Pin(5, Pin.OUT)
np = NeoPixel(dataPin, 5)
powerPin.on()
