class Color:
    """ Gives colors."""
    
    def __init__(self, red, green, blue, alpha = 255):
        """ Constructs a new Color. """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """ Gets the color as a tuple of four values (red, green, blue, alpha). """
        return (self._red, self._green, self._blue, self._alpha)   