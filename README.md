# pycom-ws2812
A module for Pycom hardware to use WS2812 RGB LEDs (commonly known as NeoPixels)

This module is designed for use on the Pycom Wipy and Lopy4 and gives functionality to drive WS2812s (NeoPixels)
Animation functions have been added to the main.py file to make it easy to create fun patterns.
Some of these patterns were translated from the NeoPixel StrandTest, and some were made up!

The basic configuration in the code is:

# Set the number of LEDs
numLed = 43
Change this to the number of LEDs in your strip.

# Initialize LEDs
chain = WS2812( ledNumber=numLed, brightness=10, dataPin='P11' ) # dataPin is for LoPy board only
The brightness value will needs to be 1-100, and can be changed later on.
The default pin is P11. On the Lopy4 this can be assigned to other pins
P11 is G22 on the Expansion Board 3.0
 
Call the Animation functions in the main loop.
