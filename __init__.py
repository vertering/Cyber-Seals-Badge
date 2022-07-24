import display
import buttons
import mch22
from machine import Pin
from neopixel import NeoPixel
import time


def reboot(pressed):
    if pressed:
        mch22.exit_python()


def single(pressed):
    if pressed:
        CyberSeals()


def infinite(pressed):
    if pressed:
        while True:
            CyberSeals()


def CyberSeals():
    np[0] = (255, 255, 0)
    np[1] = (255, 255, 0)
    np[2] = (255, 255, 0)
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    np.write()
    loop('3')
    np[0] = (255, 255, 0)
    np[1] = (255, 255, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    np.write()
    loop('2')
    np[0] = (255, 255, 0)
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    np.write()
    loop('1')
    display.drawFill(0x000000)
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
    display.drawFill(0x000000)
    display.drawText(150, 100, str(x), 0xFFF000)
    display.flush()
    time.sleep(1)


buttons.attach(buttons.BTN_A, infinite)
buttons.attach(buttons.BTN_B, single)
buttons.attach(buttons.BTN_HOME, reboot)
display.drawFill(0x000000)
display.flush()
# Pin 19 controls the power supply to SD card and neopixels
powerPin = Pin(19, Pin.OUT)
# Pin 5 is the LED's data line
dataPin = Pin(5, Pin.OUT)
# create a neopixel object for 5 pixels
np = NeoPixel(dataPin, 5)
# turn on power to the LEDs
powerPin.on()
