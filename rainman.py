# RainMan
# this class manages a LED strip and defines some lookups and color modes.
#
import adafruit_fancyled.adafruit_fancyled as fancy

class RainMan :
    def __init__( self, strip ) :
        # refer to
        # https://learn.adafruit.com/fancyled-library-for-circuitpython/led-colors
        # across the rainbow
        self.strip = strip
        self.lookup = []
        self.size = self.strip.n / 2

        grad = [ (0.0,0xFF0000), (0.33,0x00FF00), (0.67,0x0000FF), (1.0,0xFF0000)]
        palette = fancy.expand_gradient( grad, 20 )
        for index in range(self.size) :
            coloff = index / self.size
            rgb = fancy.palette_lookup( palette, coloff )
            color = rgb.pack()
            self.lookup.append( color )
        # delete to free memory grad and palette we don't them any longer
        del grad
        del palette

    def color_selected( self, coloff ) :
        coloff = coloff % 1
        colindex = int( coloff * self.size )
        return self.lookup[colindex]

    def show_static( self, coloff ) :
        color = self.color_selected( coloff )
        self.strip.fill( color )
        self.strip.show()

    def show_static_white( self ) :
        if self.strip.bpp == 4 :
            self.strip.fill((255,255,255,255))
        else :
            self.strip.fill((255,255,255))
        self.strip.show()
        
    def palette_cycle( self, coloff ) :
        for index in range( self.strip.n  ) :
            offset = coloff + ( index / self.strip.n )
            rgb = self.color_selected( offset % 1 )
            self.strip[index] = rgb
        self.strip.show()

