from ws2812 import WS2812
import utime
import uos
import pycom

# disable LED heartbeat (probably not needed in this application)
pycom.heartbeat(False)

# set the number of LEDs
numLed = 43
# initialize LEDs
chain = WS2812( ledNumber=numLed, brightness=10, dataPin='P11' ) # dataPin is for LoPy board only
# initialize LEDs Off
data = [(0,0,0)] * numLed

#######################################################
### Animation Functions -- edit at your own risk!   ###
### Scroll down for the Main Loop to edit           ###
#######################################################

# Input a value 0 to 255 to get a color value.
# The colours are a transition r - g - b - back to r.
# Do not change this!
def Wheel(WheelPos):
    WheelPos = 255 - WheelPos
    if WheelPos < 85:
        return (255 - WheelPos * 3, 0, WheelPos * 3)
    if WheelPos < 170:
        WheelPos -= 85
        return (0, WheelPos * 3, 255 - WheelPos * 3)
    WheelPos -= 170
    return (WheelPos * 3, 255 - WheelPos * 3, 0)

# Cycles all the lights through rainbow colors
def rainbow(wait):
    for j in range (0,256,1):
        for i in range (0,numLed,1):
            data[i] = Wheel((i+j & 255))
        chain.show( data )
        utime.sleep_ms(wait)

# Slightly different, this makes the rainbow equally distributed throughout
def rainbowCycle(wait):
    for j in range (0,256,1):
        for i in range (0,numLed,1):
            data[i] = Wheel(int((i * 256 / numLed) + j) & 255)
        chain.show( data )
        utime.sleep_ms(wait)

# Fill the dots one after the other with a color
def colorWipe(c, wait):
    for i in range(0, numLed, 1):
        data[i] = c
        chain.show( data )
        utime.sleep_ms(wait)

# Theatre-style crawling lights.
def theaterChase(c, wait):
    for j in range(0, 10, 1):  # do 10 cycles of chasing
        for q in range(0, 3, 1):
            for i in range(0, numLed, 3):
                try:
                    data[i+q] = c # turn every third pixel on
                except: # if i+q is out of the list then ignore
                    pass
            chain.show( data )
            utime.sleep_ms(wait)

            for i in range(0, numLed, 3):
                try:
                    data[i+q] = (0,0,0)  # turn every third pixel off
                except: # if i+q is out of the list then ignore
                    pass

def theaterChaseRainbow(wait):
    for j in range(0, 256, 1):     # cycle all 256 colors in the wheel
        for q in range(0, 3, 1):
            for i in range(0, numLed, 3):
                try:
                    data[i+q] = Wheel((i + j) % 255) #Wheel( int((i+j)) % 255)) # turn every third pixel on
                except: # if i+q is out of the list then ignore
                    pass
            chain.show( data )
            utime.sleep_ms(wait)

            for i in range(0, numLed, 3):
                try:
                    data[i+q] = (0,0,0)  # turn every third pixel off
                except: # if i+q is out of the list then ignore
                    pass

# Fill the dots one after the other with a color
def scrollWipe(wait):
    for j in range(0, 256, 16): # Transition through all colors of the wheel skip every 16 so the change is visible
        for i in range(0, numLed, 1):
            data[i] = Wheel((j) & 255)
            chain.show( data )
            utime.sleep_ms(wait)

# sparkle the LEDs to the set color
def sparkle(c, wait):
    pixel = int.from_bytes(os.urandom(1), "big") % numLed
    pixel2 = int.from_bytes(os.urandom(1), "big") % numLed
    data[pixel] = c
    data[pixel2] = c
    chain.show( data )
    utime.sleep_ms(wait)
    data[pixel] = (0,0,0)
    data[pixel2] = (0,0,0)

# Fade the brightness up  down and update a brightness parameter for other modes.
def fade(c, wait):
# Increases brightness
    for i in range(0, 50, 1):
        chain.set_brightness(i)
# Slows brightness change when dim
        #if i<20:
            #utime.sleep_ms(wait)
# Updates changes through solid()
        solid(c, 0)
    # Decreases Brightness
    for i in range(0, 50, 1):
        i = 50 - i
        chain.set_brightness(i)
        #if i<20:
            #utime.sleep_ms(wait)
        solid(c, 0)

# Display a single colour on all LEDs.
def solid(c, wait):
    for i in range(0, numLed, 1):
# Color set by user variable c and that color's position on the wheel
        data[i] = c
    chain.show( data )
    utime.sleep_ms(wait)

#######################################################
### Main Loop -- comment/edit all you like!         ###
#######################################################
while True:
    # call different animation functions from animations.py
    rainbowCycle(0) # cycles through the rainbow --rainbowCycle(wait)
    rainbow(0) # cycles all lights through the rainbow --rainbow(wait)
    theaterChaseRainbow(50) # theater chase and rainbow at the same time --theaterChaseRainbow(wait)
    chain.set_brightness(100) # change brighness (0-100), stays set --chain.set_brightness(0-100)
    colorWipe((255, 0, 0), 50) # color wipes red -- colorWipe(color, wait)
    colorWipe((0, 255, 0), 50) # color wipes Green -- colorWipe(color, wait)
    colorWipe((0, 0, 255), 50) # color wipes Blue -- colorWipe(color, wait)
    chain.set_brightness(10) # change brightness (0-100), stays set --chain.set_brightness(0-100)
    theaterChase((127, 127, 127), 50) # White -- theaterChase(color, wait)
    theaterChase((127, 0, 0), 50) # Red -- theaterChase(color, wait)
    theaterChase((0, 0, 127), 50) # Blue -- theaterChase(color, wait)
    scrollWipe(50) # scrolls through --scrollWipe(wait)
    sparkle((127, 127, 127), 5) # randomly sparkles two LEDs at a time -- sparkle(color, wait)
    fade((255, 0, 0), 50) # fades a color in and out -- fade(color, wait)
    solid((0, 0, 255), 1000) # set all LEDs to a color for a set time -- solid(color, wait)

    """
    # basic example, set lEDs individually by editing the list
    data = [(255, 0, 255),
            (255, 0, 255),
            (255, 0, 255),
            (255, 0, 255),
            (255, 0, 255),
            (255, 0, 255),
            (255, 0, 255)]
    chain.show( data )
    utime.sleep(1)
    data.append = [(0, 0, 255),
            (255, 0, 255),
            (0, 0, 255),
            (255, 0, 255),
            (0, 0, 255),
            (255, 0, 255),
            (0, 0, 255)]
    chain.show( data )
    utime.sleep(1)
    # Its critical that the list is returned to the same length as the numLed variable for the animations to work
    # If you manually edit data list then return make sure it includes all LEDs afterwards.
    data = [(0,0,0)] * numLed
    #print ("working")
    """
