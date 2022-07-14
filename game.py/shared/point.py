class Point:
    """ A distance from a relative origin (0, 0). Hold and provide information about itself. """
    
    def __init__(self, x, y):
        """ Constructs a new Point using the specified x and y values. """
        self._x = x
        self._y = y

    def add(self, other):
        """ Gets a new point that is the sum of this and the given one. """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """ Whether or not this Point is equal to the given one. """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """ Gets the horizontal distance. """
        return self._x

    def get_y(self):
        """ Gets the vertical distance. """
        return self._y

    def scale(self, factor):
        """ Scales the point by the provided factor. """
        return Point(self._x * factor, self._y * factor)