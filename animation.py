from rpi_ws281x import * # type: ignore
import time

LED_COUNT = 472
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL) # type: ignore
strip.begin()

def inclusive_range(start, end):
    return range(start - 1, end)

def off():
    for number in inclusive_range(1, 472):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

# Schweif activates from left to right. 
def schweif_turning_on(color):
    for x in inclusive_range(0, 35):
        strip.setPixelColor(282 + x, Color(*color)) # type: ignore
        strip.setPixelColor(356 + x, Color(*color)) # type: ignore
        strip.setPixelColor(355 - x, Color(*color)) # type: ignore
        

# star
def star_on(color):
    # activate full star
    for number in inclusive_range(38, 159):
        strip.setPixelColor(number, Color(*color)) # type: ignore
        
    # deactivate inside of star
    for number in inclusive_range(95, 101):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
        
    for number in inclusive_range(47, 53):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

    for number in inclusive_range(121, 126):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

    for number in inclusive_range(71, 77):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

    for number in inclusive_range(146, 150):
        strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
        
def number_turning_on(color):
    for number in inclusive_range(393, 472):
        strip.setPixelColor(number, Color(*color)) # type: ignore

# star_lines activate clockwise
def star_lines_turning_on(color):
    for number in inclusive_range(8, 37):
        strip.setPixelColor(number, Color(*color)) # type: ignore
    
    for number in inclusive_range(160, 279):
        strip.setPixelColor(number, Color(*color)) # type: ignore

while(True):
    color = (255, 255, 0)
    schweif_turning_on(color)
    strip.show()
    time.sleep(3)
    off()
    time.sleep(3)

