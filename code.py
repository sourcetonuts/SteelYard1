import time
import board
import touchio
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

num_pixels = 12

# pin usage: TRINKET: board.D4, GEMMA: board.D1
strip = neopixel.NeoPixel(
    board.D4, num_pixels, brightness = 1,
    auto_write = False, pixel_order= neopixel.RGBW )

print( "Steelyard #1 Trinket M0" )

import RainMan
display = RainMan.RainMan( strip )

import TouchMode

# Mode pin usage: TRINKET: board.A0, GEMMA: board.A1
inputMode = touchio.TouchIn( board.A0 )
modeMachine = TouchMode.TouchMode( inputMode, 3 )

inputBrightness = touchio.TouchIn( board.A3 )
brightnessMachine = TouchMode.TouchMode( inputBrightness, 5, "brightness" )
brightnessMachine.value = 1

offset = 0.001

# Loop Forever
while True :
    brightness = brightnessMachine.update()
    strip.brightness = 0.01 + ( 0.2 * brightness )
    mode = modeMachine.update()
    if mode == 0 :
        display.palette_cycle( offset )
        offset += 0.005 # 0.035 # this sets how quickly the rainbow changes (bigger is faster)
    elif mode == 1 :
        # and if just off just off paint/fill w/ the center color
        display.show_static( offset + 0.5 )
    else :
        display.show_static_white()

# end of program