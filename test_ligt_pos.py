from rpi_ws281x import * # type: ignore

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
    return range(start, end + 1)


# 1. star_lines
for number in inclusive_range(8, 17):
    strip.setPixelColor(number, Color(255, 0, 0)) # type: ignore
    
for number in inclusive_range(18, 27):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(28, 37):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
# 2. star_lines
for number in inclusive_range(160, 169):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(170, 179):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(180, 189):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
# 3. star_lines
for number in inclusive_range(190, 199):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(200, 209):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(210, 219):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
# 4. star_lines    
for number in inclusive_range(220, 229):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(230, 239):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(240, 249):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

# 5. star_lines
for number in inclusive_range(250, 259):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(260, 269):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(270, 279):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

# star on
for number in inclusive_range(38, 46):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(102, 110):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(111, 120):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(54, 61):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(62, 70):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(127, 135):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(136, 145):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(78, 85):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(86, 94):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
for number in inclusive_range(151, 159):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore
    
# star off

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

# schweif
for number in inclusive_range(282, 318):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

for number in inclusive_range(319, 355):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

for number in inclusive_range(356, 392):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore

# number
for number in inclusive_range(393, 472):
    strip.setPixelColor(number, Color(0, 0, 0)) # type: ignore



strip.show()
