# Steel Yard v1
Provides the software function for the Lamp Building class

## Hardware

### Adafruit Trinket M0
https://www.adafruit.com/product/3500

#### USB Cable for Power (good enough for 12 LEDs as-is)
This is the simplest and w/ only 12 LEDS can power from a computer or any USB charger.
If you add LEDs to a different Neopixel you may want to one of more of the following:
- change brightness in the software
- bring in Power on Battery or USB pin rather than connector (read the docs for safety, etc)
- Power Neopixl differently based on your choices
- addi hardware: a barrel jack power input and switch

#### Consder adding a on/off switch

### Adafruit Neo Pixel of choice

Tested:
- NeoPixel Ring - 12 x 5050 RGBW LEDs w/ Integrated Drivers - Warm White - ~3000K
- TBD

### Wiring

#### Neopixel 3 wires 5V, GND and Data In
Get the 5V from USB, GND from the GND pin and use D4 for the Neopixel Data

#### Wire button 1 to isolated capacitence material (CAPTOUCH)
Button 2 has 3 modes: rainbow to selected color, display all LEDs in selected color and white leds. Touching toggles to the next mode in the sequence.

#### Wire button 2 to isolated capacitence material (CAPTOUCH) 
This is optional and if you leave it off you probably want to change the software to ignore it and have a default brightness.
Button 2 supports 5 levels of brightness. Touching toggles to the next brighest and the back to the dim setting.
