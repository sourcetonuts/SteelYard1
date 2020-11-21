# TouchMode
# this class manages a single captouch pin and cycles through modes
# on that pin up to provided lastmode
#
import time

class TouchMode :
    def __init__( self, inputMode, num = 2, name = None ) :
        self.value = 0
        self.lastmode = num - 1
        self.input = inputMode
        self.name = name or "mode"

    def update( self ) :
        wasoff = not self.input.value
        time.sleep(0.005)  # 5ms delay for debounce
        if not wasoff and self.input.value :
            # just touched button
            time.sleep(0.005)  # 5ms delay for debounce
            if self.value >= self.lastmode :
                self.value = 0
            else :
                self.value = self.value + 1
            # debounce
            time.sleep( 0.5 )
            print( self.name + " {}".format( self.value ) )
        return self.value