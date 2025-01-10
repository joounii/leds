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

for number in inclusive_range(1, 472):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
strip.show()
