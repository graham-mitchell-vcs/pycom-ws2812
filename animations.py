###################################################################################
# this is for reference only if you decide to remove animations from your main.py #
###################################################################################
# animations based on common Neopixel animations, and some not so common


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

# Cycles all the lights through the same rainbow colors
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
        solid(c)
    # Decreases Brightness
    for i in range(0, 50, 1):
        i = 50 - i
        chain.set_brightness(i)
        #if i<20:
            #utime.sleep_ms(wait)
        solid(c)

# Display a single colour on all LEDs.
def solid(c, wait):
    for i in range(0, numLed, 1):
# Color set by user variable c and that color's position on the wheel
        data[i] = c
    chain.show( data )
    utime.sleep_ms(wait)
