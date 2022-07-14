import pyray
from shared.point import Point

class KeyboardService:
    """ Detects player input. """

    def __init__(self, cell_size = 1):
        """ Constructs a new KeyboardService using the specified cell size. """
        self._cell_size = cell_size

    def get_direction(self):
        """ Gets the selected direction based on the currently pressed keys for the first player. """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_A):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_D):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_W):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_S):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction

    def get_direction2(self):
        """ Gets the selected direction based on the currently pressed keys for the second player. """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_J):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_L):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_I):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_K):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction    

    def move_direction(self):
        """ Gets the selected direction based on the currently pressed keys. """
        dx = 0
        dy = 0

       
        dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction