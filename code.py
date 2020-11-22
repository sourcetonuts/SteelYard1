import board
import touchio
import neopixel

print( "Steelyard #1 Trinket M0" )

# make the strip and here a 12 LED NeoPixel strip (can be dotstar, etc. w/ libraries)
strip = neopixel.NeoPixel(
    board.D4, 12, brightness = 1.0,
    auto_write = False, pixel_order= neopixel.RGBW )

# Kenny's Display classs, It uses strip passed and libraries: adafruit_fancyled
import MyPy.rainman
display = MyPy.rainman.RainMan( strip )

# Kenny's TouchMode class, It uses touchio passed and libraries: time
import MyPy.touchmode

# handles the application's Mode:
# 0:rainbow select
# 1:display selected color
# 2:white light
inputMode = touchio.TouchIn( board.A0 )
modeMachine = MyPy.touchmode.TouchMode( inputMode, 3 )

# handles the application's brightness:
# 0: dimmest
# 1-4: inceasing brightness
inputBrightness = touchio.TouchIn( board.A3 )
brightnessMachine = MyPy.touchmode.TouchMode( inputBrightness, 5, "brightness" )
brightnessMachine.value = 1

offset = 0

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